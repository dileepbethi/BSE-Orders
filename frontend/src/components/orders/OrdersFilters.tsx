function OrdersFilters() {

  return (

    <div className="grid grid-cols-5 gap-4 rounded-2xl border border-slate-800 bg-slate-900 p-5">

      <select className="rounded-xl border border-slate-700 bg-slate-800 p-3 text-white">

        <option>Exchange</option>

        <option>BSE</option>

        <option>NSE</option>

      </select>

      <select className="rounded-xl border border-slate-700 bg-slate-800 p-3 text-white">

        <option>Status</option>

        <option>Processed</option>

        <option>Pending</option>

      </select>

      <select className="rounded-xl border border-slate-700 bg-slate-800 p-3 text-white">

        <option>Domestic</option>

        <option>Domestic</option>

        <option>International</option>

      </select>

      <input
        type="date"
        className="rounded-xl border border-slate-700 bg-slate-800 p-3 text-white"
      />

      <button
        className="rounded-xl bg-blue-600 font-medium text-white hover:bg-blue-700"
      >
        Apply Filters
      </button>

    </div>

  );

}

export default OrdersFilters;