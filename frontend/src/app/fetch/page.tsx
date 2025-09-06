'use client';

import { useEffect, useState } from 'react';
import { fetchCVEData } from '@/utils/api';
import DataCard from '@/components/DataCard';
import { CVEData } from '@/types/data';

export default function FetchPage() {
  const [data, setData] = useState<{ message: string; data: CVEData[] } | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await fetchCVEData();
      setData(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch CVE data');
    } finally {
      setLoading(false);
    }
  };

  const getSeverityColor = (severity?: string) => {
    switch (severity?.toLowerCase()) {
      case 'critical':
        return 'text-red-600';
      case 'high':
        return 'text-orange-600';
      case 'medium':
        return 'text-yellow-600';
      case 'low':
        return 'text-green-600';
      default:
        return 'text-gray-600';
    }
  };

  if (loading) return (
    <div className="flex justify-center items-center min-h-[60vh]">
      <div className="animate-pulse text-lg text-gray-600">Loading CVE data...</div>
    </div>
  );

  if (error) return (
    <div className="flex justify-center items-center min-h-[60vh]">
      <div className="text-red-500 bg-red-50 p-4 rounded-lg border border-red-200">
        <h3 className="font-semibold mb-2">Error Loading Data</h3>
        <p>{error}</p>
      </div>
    </div>
  );

  return (
    <div className="container mx-auto p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">CVE Data Feed</h1>
        <button 
          onClick={loadData}
          className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-md transition flex items-center gap-2"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Refresh Data
        </button>
      </div>

      {data?.data && data.data.length > 0 ? (
        <div className="grid gap-6">
          {data.data.map((item: CVEData, index: number) => (
            <DataCard key={item.id || index} title={item.id || `CVE Entry ${index + 1}`}>
              <div className="space-y-4">
                <div className="flex justify-between items-start">
                  <div className="flex-1">
                    <p className="text-gray-700 mb-2">{item.description}</p>
                    <div className="flex gap-2 items-center">
                      <span className={`font-semibold ${getSeverityColor(item.severity)}`}>
                        {item.severity?.toUpperCase() || 'N/A'}
                      </span>
                      {item.published && (
                        <span className="text-gray-500 text-sm">
                          Published: {new Date(item.published).toLocaleDateString()}
                        </span>
                      )}
                    </div>
                  </div>
                  {item.score !== undefined && (
                    <div className={`px-4 py-2 rounded-full font-bold ${
                      item.score >= 7 ? 'bg-red-100 text-red-700' :
                      item.score >= 4 ? 'bg-yellow-100 text-yellow-700' :
                      'bg-green-100 text-green-700'
                    }`}>
                      Score: {item.score}
                    </div>
                  )}
                </div>
                {item.references && item.references.length > 0 && (
                  <div className="mt-4">
                    <h4 className="text-sm font-semibold text-gray-700 mb-2">References:</h4>
                    <ul className="list-disc list-inside space-y-1">
                      {item.references.map((ref, idx) => (
                        <li key={idx} className="text-sm text-blue-600 hover:underline">
                          <a href={ref} target="_blank" rel="noopener noreferrer">{ref}</a>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </DataCard>
          ))}
        </div>
      ) : (
        <div className="text-center text-gray-500 py-12">
          No CVE data available. Click refresh to fetch latest data.
        </div>
      )}
    </div>
  );
}
