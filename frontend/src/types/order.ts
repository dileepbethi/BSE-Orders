export type Order = {
  id: number;

  company: string;

  customer: string;

  announcement_date: string;

  announcement_type: string;

  order_value: string;

  source_file: string;

  exchange: string;

  confidence_score: number;

  processing_status: string;

  created_at: string;
};