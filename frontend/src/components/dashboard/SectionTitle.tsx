type SectionTitleProps = {
  title: string;
  subtitle: string;
};

function SectionTitle({
  title,
  subtitle,
}: SectionTitleProps) {
  return (
    <div className="mb-4">
      <h3 className="text-lg font-semibold text-white">
        {title}
      </h3>

      <p className="text-sm text-slate-400">
        {subtitle}
      </p>
    </div>
  );
}

export default SectionTitle;