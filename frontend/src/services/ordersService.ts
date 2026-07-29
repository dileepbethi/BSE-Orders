import { api } from "./api";

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

export async function getOrders(
  page: number = 1,
  limit: number = 10
): Promise<Order[]> {

  const response = await api.get(
    `/orders?page=${page}&limit=${limit}`
  );

  return response.data;
}
export async function searchOrders(query: string): Promise<Order[]> {

  const response = await api.get(
    `/search?query=${encodeURIComponent(query)}`
  );

  return response.data;
}