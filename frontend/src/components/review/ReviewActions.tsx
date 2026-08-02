function ReviewActions() {

  return (

    <div className="mt-6 flex gap-4">

      <button className="rounded-xl bg-emerald-600 px-6 py-3 font-semibold text-white hover:bg-emerald-700">

        Approve

      </button>

      <button className="rounded-xl bg-red-600 px-6 py-3 font-semibold text-white hover:bg-red-700">

        Reject

      </button>

      <button className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white hover:bg-blue-700">

        Save Changes

      </button>

    </div>

  );

}

export default ReviewActions;