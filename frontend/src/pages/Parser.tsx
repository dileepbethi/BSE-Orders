import PageHeader from "../components/common/PageHeader";

function Parser() {
  return (
    <>
      <PageHeader
        title="Parser"
        subtitle="Automation Status"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-10">

        <h2 className="text-2xl font-semibold text-white">
          Parser Dashboard
        </h2>

        <p className="mt-3 text-slate-400">
          Parser activity, logs, downloads and processing statistics will be
          displayed here.
        </p>

      </div>
    </>
  );
}

export default Parser;