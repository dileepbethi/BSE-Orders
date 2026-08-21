import { api } from "./api";

/* =========================================
   Dashboard Statistics
========================================= */

export type DashboardStats = {
  total_orders: number;
  total_companies: number;
  domestic_orders: number;
  international_orders: number;
};

export async function getDashboardStats(): Promise<DashboardStats> {

  const response = await api.get(
    "/dashboard/stats"
  );

  return response.data;
}

/* =========================================
   Monthly Orders
========================================= */

export type MonthlyOrder = {
  month: string;
  value: number;
};

export async function getMonthlyOrders(): Promise<MonthlyOrder[]> {

  const response = await api.get(
    "/dashboard/monthly-orders"
  );

  return response.data;
}