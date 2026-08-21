import PageHeader from "../components/common/PageHeader";

function Analytics() {
  return (
    <>
      <PageHeader
        title="Analytics"
        subtitle="Business Intelligence"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-10">

        <h2 className="text-2xl font-semibold text-white">
          Analytics
        </h2>

        <p className="mt-3 text-slate-400">
          Trends, company rankings, sector insights and historical analytics
          will appear here.
        </p>

      </div>
    </>
  );
}

export default Analytics;