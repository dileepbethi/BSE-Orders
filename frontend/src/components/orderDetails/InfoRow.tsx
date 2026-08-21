type Props = {
  label: string;
  value: React.ReactNode;
};

function InfoRow({
  label,
  value,
}: Props) {
  return (
    <div className="grid grid-cols-[180px_1fr] border-b border-slate-800 py-3 last:border-none">

      <div className="text-sm text-slate-400">
        {label}
      </div>

      <div className="font-medium text-white">
        {value}
      </div>

    </div>
  );
}

export default InfoRow;