type Props = {
  status: string;
};

function StatusBadge({
  status,
}: Props) {
  const color =
    status === "SUCCESS"
      ? "bg-emerald-600"
      : "bg-amber-500";

  return (
    <span
      className={`${color} rounded-full px-4 py-1 text-sm font-semibold text-white`}
    >
      {status}
    </span>
  );
}

export default StatusBadge;