import { useEffect, useState } from "react";

import PageHeader from "../components/common/PageHeader";
import KPICard from "../components/dashboard/KPICard";
import ChartCard from "../components/dashboard/ChartCard";
import PieChartCard from "../components/dashboard/PieChartCard";
import OrdersTable from "../components/dashboard/OrdersTable";

import { getDashboardStats } from "../services/dashboardService";
import type { DashboardStats } from "../services/dashboardService";
function Dashboard() {
  const [stats, setStats] = useState<DashboardStats>({
    total_records: 0,
    total_companies: 0,
    total_customers: 0,
    total_orders: 0,
  });

  useEffect(() => {
    getDashboardStats()
      .then(setStats)
      .catch((error) => {
        console.error("Dashboard API Error:", error);
      });
  }, []);

  return (
    <>
      <PageHeader
        title="Executive Dashboard"
        subtitle="Procurement Intelligence Platform"
      />

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
        <KPICard
          title="Total Orders"
          value={stats.total_orders.toString()}
          footer="Orders detected"
        />

        <KPICard
          title="Total Companies"
          value={stats.total_companies.toString()}
          footer="Unique companies"
        />

        <KPICard
          title="Total Records"
          value={stats.total_records.toString()}
          footer="Announcements processed"
        />

        <KPICard
          title="Total Customers"
          value={stats.total_customers.toString()}
          footer="Unique customers"
        />
      </div>

      <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <ChartCard
            title="Monthly Order Trend"
            subtitle="Coming in next step"
          />
        </div>

        <PieChartCard
          title="Order Distribution"
          subtitle="Coming in next step"
        />
      </div>

      <div className="mt-8">
        <OrdersTable />
      </div>
    </>
  );
}

export default Dashboard;