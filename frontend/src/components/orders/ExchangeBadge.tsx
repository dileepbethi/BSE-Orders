type Props = {
  exchange: string;
};

function ExchangeBadge({
  exchange,
}: Props) {

  const color =
    exchange === "BSE"
      ? "bg-blue-500/20 text-blue-400"
      : "bg-orange-500/20 text-orange-400";

  return (
    <span
      className={`rounded-full px-3 py-1 text-xs font-semibold ${color}`}
    >
      {exchange}
    </span>
  );
}

export default ExchangeBadge;