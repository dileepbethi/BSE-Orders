type Props = {
  title: string;
  children: React.ReactNode;
};

function SectionCard({
  title,
  children,
}: Props) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-900">
      <div className="border-b border-slate-700 px-6 py-4">
        <h2 className="text-lg font-semibold text-white">
          {title}
        </h2>
      </div>

      <div className="p-6">
        {children}
      </div>
    </div>
  );
}

export default SectionCard;