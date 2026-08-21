import Card from "../ui/Card";

type KPICardProps = {
  title: string;
  value: string;
  footer: string;
};

function KPICard({
  title,
  value,
  footer,
}: KPICardProps) {
  return (
    <Card>
      <p className="text-xs uppercase tracking-wider text-slate-400">
        {title}
      </p>

      <h2 className="mt-3 text-3xl font-bold text-white">
        {value}
      </h2>

      <p className="mt-4 text-sm text-emerald-400">
        {footer}
      </p>
    </Card>
  );
}

export default KPICard;