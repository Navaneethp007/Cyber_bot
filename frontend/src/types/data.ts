export interface CVEData {
  id?: string;
  description?: string;
  severity?: string;
  published?: string;
  references?: string[];
  score?: number;
  vector?: string;
  affected_systems?: string[];
  [key: string]: string | number | string[] | undefined; // More specific type union
}

export interface AnalysisData {
  summary?: string;
  details?: string;
  recommendations?: string[];
  severity_distribution?: Record<string, number>;
  threat_categories?: string[];
  risk_score?: number;
  [key: string]: string | number | string[] | Record<string, number> | undefined;
}

export interface NotificationResponse {
  message: string;
  status?: 'success' | 'error' | 'pending';
  timestamp?: string;
}
