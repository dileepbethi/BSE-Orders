type Props = {
  company: string;
  customer?: string;
};

function CompanyCell({
  company,
  customer,
}: Props) {
  return (
    <div>
      <div className="font-semibold text-white">
        {company}
      </div>

      <div className="mt-1 text-xs text-slate-400">
        {customer || "No customer"}
      </div>
    </div>
  );
}

export default CompanyCell;