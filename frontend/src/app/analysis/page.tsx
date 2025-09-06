'use client';

import { useEffect, useState } from 'react';
import { fetchAnalysis } from '@/utils/api';
import DataCard from '@/components/DataCard';
import { AnalysisData } from '@/types/data';

export default function AnalysisPage() {
  const [data, setData] = useState<{ message: string; data: AnalysisData } | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await fetchAnalysis();
      setData(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch analysis');
    } finally {
      setLoading(false);
    }
  };

  const renderSeverityDistribution = (distribution?: Record<string, number>) => {
    if (!distribution) return null;

    const getColor = (severity: string) => {
      switch (severity.toLowerCase()) {
        case 'critical': return 'bg-red-500';
        case 'high': return 'bg-orange-500';
        case 'medium': return 'bg-yellow-500';
        case 'low': return 'bg-green-500';
        default: return 'bg-gray-500';
      }
    };

    const total = Object.values(distribution).reduce((acc, curr) => acc + curr, 0);

    return (
      <div className="space-y-3">
        <h3 className="font-semibold text-gray-700">Severity Distribution</h3>
        <div className="space-y-2">
          {Object.entries(distribution).map(([severity, count]) => (
            <div key={severity} className="space-y-1">
              <div className="flex justify-between text-sm">
                <span className="font-medium">{severity.toUpperCase()}</span>
                <span>{Math.round((count / total) * 100)}% ({count})</span>
              </div>
              <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
                <div
                  className={`h-full ${getColor(severity)} transition-all duration-500`}
                  style={{ width: `${(count / total) * 100}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  };

  if (loading) return (
    <div className="flex justify-center items-center min-h-[60vh]">
      <div className="animate-pulse text-lg text-gray-600">Loading analysis...</div>
    </div>
  );

  if (error) return (
    <div className="flex justify-center items-center min-h-[60vh]">
      <div className="text-red-500 bg-red-50 p-4 rounded-lg border border-red-200">
        <h3 className="font-semibold mb-2">Error Loading Analysis</h3>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mx-auto p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Threat Analysis</h1>
        <button 
          onClick={loadData}
          className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-md transition flex items-center gap-2"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh Analysis
        </button>
      </div>

      {data?.data ? (
        <div className="grid gap-6 md:grid-cols-2">
          {/* Summary Card */}
          <DataCard title="Summary">
            <div className="prose max-w-none">
              <p className="text-gray-700">{data.data.summary}</p>
              {data.data.risk_score !== undefined && (
                <div className="mt-4">
                  <h3 className="font-semibold text-gray-700 mb-2">Risk Score</h3>
                  <div className={`inline-flex items-center px-4 py-2 rounded-full font-bold ${
                    data.data.risk_score >= 7 ? 'bg-red-100 text-red-700' :
                    data.data.risk_score >= 4 ? 'bg-yellow-100 text-yellow-700' :
                    'bg-green-100 text-green-700'
                  }`}>
                    {data.data.risk_score.toFixed(1)} / 10
                  </div>
                </div>
              )}
            </div>
          </DataCard>

          {/* Severity Distribution Card */}
          <DataCard title="Statistics">
            {renderSeverityDistribution(data.data.severity_distribution)}
          </DataCard>

          {/* Detailed Analysis Card */}
          <div className="md:col-span-2">
            <DataCard title="Detailed Analysis">
              <div className="space-y-6">
                <div className="prose max-w-none">
                  <p className="text-gray-700 whitespace-pre-line">{data.data.details}</p>
                </div>

                {data.data.threat_categories && data.data.threat_categories.length > 0 && (
                  <div className="mt-4">
                    <h3 className="font-semibold text-gray-700 mb-2">Threat Categories</h3>
                    <div className="flex flex-wrap gap-2">
                      {data.data.threat_categories.map((category, index) => (
                        <span key={index} className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
                          {category}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {data.data.recommendations && data.data.recommendations.length > 0 && (
                  <div className="mt-6">
                    <h3 className="font-semibold text-gray-700 mb-3">Recommendations</h3>
                    <ul className="list-disc list-inside space-y-2">
                      {data.data.recommendations.map((rec, index) => (
                        <li key={index} className="text-gray-700">{rec}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </DataCard>
          </div>
        </div>
      ) : (
        <div className="text-center text-gray-500 py-12">
          No analysis data available. Click refresh to fetch latest analysis.
        </div>
      )}
    </div>
  );
}
