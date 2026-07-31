import PageHeader from "../components/common/PageHeader";

function Companies() {
  return (
    <>
      <PageHeader
        title="Companies"
        subtitle="Company Intelligence"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-10">

        <h2 className="text-2xl font-semibold text-white">
          Companies Module
        </h2>

        <p className="mt-3 text-slate-400">
          Company profiles, historical orders, rankings, customers and analytics
          will appear here.
        </p>

      </div>
    </>
  );
}

export default Companies;