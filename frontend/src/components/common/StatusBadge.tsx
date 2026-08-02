type Props = {
  status: string;
};

function StatusBadge({ status }: Props) {

  const normalized = status.toLowerCase();

  let styles =
    "bg-slate-700 text-white";

  if (
    normalized.includes("processed")
  ) {

    styles =
      "bg-emerald-600 text-white";

  } else if (
    normalized.includes("pending")
  ) {

    styles =
      "bg-yellow-500 text-black";

  } else if (
    normalized.includes("failed")
  ) {

    styles =
      "bg-red-600 text-white";

  }

  return (

    <span
      className={`rounded-full px-3 py-1 text-xs font-semibold ${styles}`}
    >
      {status}
    </span>

  );

}

export default StatusBadge;