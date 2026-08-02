function TopHeader() {

  return (

    <header
      className="
        sticky
        top-0
        z-30
        flex
        h-16
        items-center
        justify-between
        border-b
        border-slate-800
        bg-slate-900/95
        px-8
        backdrop-blur
      "
    >

      <input
        type="text"
        placeholder="Search companies, customers, orders..."
        className="
          w-96
          rounded-xl
          border
          border-slate-700
          bg-slate-800
          px-4
          py-2
          text-white
          outline-none
          focus:border-blue-500
        "
      />

      <div className="flex items-center gap-4">

        <button
          className="
            rounded-xl
            bg-blue-600
            px-5
            py-2
            font-medium
            text-white
            transition
            hover:bg-blue-700
          "
        >
          + New Order
        </button>

        <button
          className="
            rounded-full
            bg-slate-800
            p-3
            text-xl
            hover:bg-slate-700
          "
        >
          🔔
        </button>

      </div>

    </header>

  );

}

export default TopHeader;