function TopHeader() {
  return (
    <header className="flex h-16 items-center justify-between border-b border-slate-700 bg-slate-900 px-6">
      <div>
        <input
          type="text"
          placeholder="Search companies, orders..."
          className="w-80 rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-white outline-none"
        />
      </div>

      <div className="flex items-center gap-4">
        <button className="rounded-lg bg-blue-600 px-4 py-2 font-semibold text-white hover:bg-blue-700">
          + New Announcement
        </button>

        <span className="text-2xl">🔔</span>
      </div>
    </header>
  );
}

export default TopHeader;