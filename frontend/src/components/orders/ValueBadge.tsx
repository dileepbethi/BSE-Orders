type Props = {
  value?: string;
};

function ValueBadge({ value }: Props) {
  if (!value) {
    return (
      <span className="text-slate-500">
        —
      </span>
    );
  }

  return (
    <span className="rounded-full bg-emerald-500/20 px-3 py-1 text-sm font-semibold text-emerald-400">
      ₹ {value}
    </span>
  );
}

export default ValueBadge;