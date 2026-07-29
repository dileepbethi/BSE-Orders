import { api } from "./api";

export type DashboardStats = {
  total_records: number;
  total_companies: number;
  total_customers: number;
  total_orders: number;
};

export async function getDashboardStats(): Promise<DashboardStats> {
  const response = await api.get("/stats");
  return response.data;
}