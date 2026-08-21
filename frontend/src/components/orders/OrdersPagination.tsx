type Props = {
  page: number;
  pages: number;
  onPageChange: (page: number) => void;
};

function OrdersPagination({
  page,
  pages,
  onPageChange,
}: Props) {

  const pageNumbers = Array.from(
    { length: pages },
    (_, i) => i + 1
  );

  return (

    <div className="flex items-center justify-between rounded-xl border border-slate-700 bg-slate-900 p-5">

      <button
        disabled={page === 1}
        onClick={() => onPageChange(page - 1)}
        className="rounded-lg bg-slate-800 px-4 py-2 text-white disabled:opacity-40"
      >
        Previous
      </button>

      <div className="flex gap-2">

        {pageNumbers.map((number) => (

          <button
            key={number}
            onClick={() => onPageChange(number)}
            className={
              number === page
                ? "rounded-lg bg-blue-600 px-4 py-2 text-white"
                : "rounded-lg bg-slate-800 px-4 py-2 text-white hover:bg-slate-700"
            }
          >
            {number}
          </button>

        ))}

      </div>

      <button
        disabled={page === pages}
        onClick={() => onPageChange(page + 1)}
        className="rounded-lg bg-slate-800 px-4 py-2 text-white disabled:opacity-40"
      >
        Next
      </button>

    </div>

  );

}

export default OrdersPagination;