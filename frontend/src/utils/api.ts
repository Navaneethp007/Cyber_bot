import { CVEData, AnalysisData, NotificationResponse } from '@/types/data';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function fetchCVEData(): Promise<{ message: string; data: CVEData[] }> {
  try {
    const response = await fetch(`${API_BASE_URL}/fetch`);
    if (!response.ok) throw new Error('Failed to fetch CVE data');
    return await response.json();
  } catch (error) {
    console.error('Error fetching CVE data:', error);
    throw error;
  }
}

export async function fetchAnalysis(): Promise<{ message: string; data: AnalysisData }> {
  try {
    const response = await fetch(`${API_BASE_URL}/analysis`);
    if (!response.ok) throw new Error('Failed to fetch analysis');
    return await response.json();
  } catch (error) {
    console.error('Error fetching analysis:', error);
    throw error;
  }
}

export async function sendNotification(): Promise<NotificationResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/notify`);
    if (!response.ok) throw new Error('Failed to send notification');
    return await response.json();
  } catch (error) {
    console.error('Error sending notification:', error);
    throw error;
  }
}
