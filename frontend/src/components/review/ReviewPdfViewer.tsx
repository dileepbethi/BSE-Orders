function ReviewPdfViewer() {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-5">

      <div className="mb-4 flex items-center justify-between">

        <h2 className="text-lg font-semibold text-white">
          Original PDF
        </h2>

        <button className="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white hover:bg-blue-700">
          Open PDF
        </button>

      </div>

      <div className="flex h-[700px] items-center justify-center rounded-xl border border-slate-700 bg-slate-800">

        <span className="text-slate-500">
          PDF Preview
        </span>

      </div>

    </div>
  );
}

export default ReviewPdfViewer;