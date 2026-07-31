import PageHeader from "../components/common/PageHeader";

function ReviewQueue() {
  return (
    <>
      <PageHeader
        title="Review Queue"
        subtitle="AI Validation"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-10">

        <h2 className="text-2xl font-semibold text-white">
          Review Queue
        </h2>

        <p className="mt-3 text-slate-400">
          Pending AI extracted announcements will be reviewed from this page.
        </p>

      </div>
    </>
  );
}

export default ReviewQueue;