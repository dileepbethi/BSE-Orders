import { useEffect, useState } from "react";

import PageHeader from "../components/common/PageHeader";
import KPICard from "../components/dashboard/KPICard";
import ChartCard from "../components/dashboard/ChartCard";
import PieChartCard from "../components/dashboard/PieChartCard";

import { api } from "../services/api";

type DashboardStats = {
  total_orders: number;
  total_companies: number;
  domestic_orders: number;
  international_orders: number;
};

function Dashboard() {
  const [stats, setStats] = useState<DashboardStats>({
    total_orders: 0,
    total_companies: 0,
    domestic_orders: 0,
    international_orders: 0,
  });

  useEffect(() => {
    api
      .get("/dashboard/stats")
      .then((response) => {
        setStats(response.data);
      })
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
          footer="Orders available in database"
        />

        <KPICard
          title="Total Companies"
          value={stats.total_companies.toString()}
          footer="Unique listed companies"
        />

        <KPICard
          title="Domestic Orders"
          value={stats.domestic_orders.toString()}
          footer="Domestic contracts"
        />

        <KPICard
          title="International Orders"
          value={stats.international_orders.toString()}
          footer="International contracts"
        />
      </div>

      <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <ChartCard
            title="Monthly Order Trend"
            subtitle="Aggregate value of contract announcements"
          />
        </div>

        <PieChartCard
          title="Sector Distribution"
          subtitle="Orders by sector"
        />
      </div>
    </>
  );
}

export default Dashboard;