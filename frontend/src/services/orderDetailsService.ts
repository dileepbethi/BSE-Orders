import { api } from "./api";

export type OrderDetails = {
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

export async function getOrderDetails(
  id: number
): Promise<OrderDetails> {

  const response = await api.get(`/orders/${id}`);

  return response.data;
}