import { api } from "./api";

export type OrderDetails = {
  id: number;

  company: string;

  customer: string;

  announcement_date: string;

  announcement_type: string;

  order_value: string;

  order_value_crore: number;

  awarding_entity: string;

  execution_period: string;

  order_type: string;

  domestic: string;

  project_description: string;

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

export async function updateOrder(
  id: number,
  data: Partial<OrderDetails>
): Promise<void> {

  await api.put(
    `/orders/${id}`,
    data
  );

}