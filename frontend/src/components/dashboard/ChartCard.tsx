import Card from "../ui/Card";
import SectionTitle from "./SectionTitle";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { monthlyOrders } from "../../data/dashboardData";

type ChartCardProps = {
  title: string;
  subtitle: string;
};

function ChartCard({
  title,
  subtitle,
}: ChartCardProps) {
  return (
    <Card>
      <SectionTitle
        title={title}
        subtitle={subtitle}
      />

      <div className="h-72">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={monthlyOrders}>
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