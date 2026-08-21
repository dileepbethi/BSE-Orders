import Card from "../ui/Card";
import SectionTitle from "./SectionTitle";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { sectorDistribution } from "../../data/dashboardData";

const COLORS = [
  "#3b82f6",
  "#10b981",
  "#f59e0b",
  "#8b5cf6",
];

type Props = {
  title: string;
  subtitle: string;
};

function PieChartCard({
  title,
  subtitle,
}: Props) {
  return (
    <Card>
      <SectionTitle
        title={title}
        subtitle={subtitle}
      />

      <div className="h-72">
        <ResponsiveContainer>
          <PieChart>
            <Pie
              data={sectorDistribution}
              dataKey="value"
              nameKey="name"
              outerRadius={90}
            >
              {sectorDistribution.map((_, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index % COLORS.length]}
                />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </Card>
  );
}

export default PieChartCard;