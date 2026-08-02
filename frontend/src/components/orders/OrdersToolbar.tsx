function OrdersToolbar() {

  return (

    <div className="flex items-center justify-between rounded-2xl border border-slate-800 bg-slate-900 p-5">

      <div>

        <h2 className="text-xl font-semibold text-white">
          Enterprise Order Management
        </h2>

        <p className="mt-1 text-sm text-slate-400">
          Search, review and validate procurement announcements.
        </p>

      </div>

      <div className="flex gap-3">

        <button
          className="rounded-xl border border-slate-700 px-5 py-2 text-white hover:bg-slate-800"
        >
          Export CSV
        </button>

        <button
          className="rounded-xl bg-blue-600 px-5 py-2 font-medium text-white hover:bg-blue-700"
        >
          + Import
        </button>

      </div>

    </div>

  );

}

export default OrdersToolbar;