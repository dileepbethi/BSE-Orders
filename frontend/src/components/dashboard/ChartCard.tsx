import { useEffect, useState } from "react";

import Card from "../ui/Card";
import SectionTitle from "./SectionTitle";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
} from "recharts";

import {
  getMonthlyOrders,
  type MonthlyOrder,
} from "../../services/dashboardService";

type ChartCardProps = {
  title: string;
  subtitle: string;
};

function ChartCard({
  title,
  subtitle,
}: ChartCardProps) {

  const [data, setData] = useState<MonthlyOrder[]>([]);

  useEffect(() => {

    getMonthlyOrders()
      .then(setData)
      .catch((error) => {
        console.error("Monthly Orders API Error:", error);
      });

  }, []);

  return (

    <Card>

      <SectionTitle
        title={title}
        subtitle={subtitle}
      />

      <div className="h-72">

        <ResponsiveContainer width="100%" height="100%">

          <LineChart data={data}>

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="value"
              stroke="#3b82f6"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </Card>

  );

}

export default ChartCard;