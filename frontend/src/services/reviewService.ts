import { api } from "./api";

export type Review = {
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

export async function getPendingReviews(): Promise<Review[]> {

  const response = await api.get(
    "/review/pending"
  );

  return response.data;

}

export async function getReview(
  id: number
): Promise<Review> {

  const response = await api.get(
    `/review/${id}`
  );

  return response.data;

}