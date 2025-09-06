'use client';

import { useState } from 'react';
import { sendNotification } from '@/utils/api';
import DataCard from '@/components/DataCard';
import { NotificationResponse } from '@/types/data';

export default function NotifyPage() {
  const [result, setResult] = useState<NotificationResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleNotify = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await sendNotification();
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to send notification');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">Notification Center</h1>
      <div className="mb-8">
        <button
          onClick={handleNotify}
          disabled={loading}
          className={`${
            loading ? 'bg-gray-400' : 'bg-blue-500 hover:bg-blue-600'
          } text-white px-6 py-3 rounded-md transition`}
        >
          {loading ? 'Sending...' : 'Send Notification'}
        </button>
      </div>

      {error && (
        <DataCard title="Error">
          <div className="text-red-500">{error}</div>
        </DataCard>
      )}

      {result && (
        <DataCard title="Notification Status">
          <pre className="whitespace-pre-wrap">{JSON.stringify(result, null, 2)}</pre>
        </DataCard>
      )}
    </div>
  );
}
