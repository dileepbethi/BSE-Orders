import { useEffect, useState } from "react";

type Props = {
  review: any;
};

function ReviewInfoPanel({ review }: Props) {

  const [company, setCompany] = useState("");
  const [customer, setCustomer] = useState("");
  const [orderValue, setOrderValue] = useState("");
  const [awardingEntity, setAwardingEntity] = useState("");
  const [execution, setExecution] = useState("");
  const [orderType, setOrderType] = useState("");

  useEffect(() => {

    if (!review) return;

    setCompany(review.company || "");
    setCustomer(review.customer || "");
    setOrderValue(review.order_value || "");
    setAwardingEntity(review.awarding_entity || "");
    setExecution(review.execution_period || "");
    setOrderType(review.order_type || "");

  }, [review]);

  return (

    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-lg font-semibold text-white">
        AI Extracted Information
      </h2>

      <div className="space-y-5">

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Company
          </label>

          <input
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Customer
          </label>

          <input
            value={customer}
            onChange={(e) => setCustomer(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Order Value
          </label>

          <input
            value={orderValue}
            onChange={(e) => setOrderValue(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Awarding Entity
          </label>

          <input
            value={awardingEntity}
            onChange={(e) => setAwardingEntity(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Execution Period
          </label>

          <input
            value={execution}
            onChange={(e) => setExecution(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Order Type
          </label>

          <input
            value={orderType}
            onChange={(e) => setOrderType(e.target.value)}
            className="w-full rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none"
          />

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Domestic
          </label>

          <div className="rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 text-white">
            {review?.domestic || "-"}
          </div>

        </div>

        <div>

          <label className="mb-2 block text-xs text-slate-400">
            Confidence
          </label>

          <div className="rounded-xl border border-slate-700 bg-slate-800 px-4 py-3 font-semibold text-yellow-400">
            {review?.confidence_score ?? "-"}%
          </div>

        </div>

      </div>

    </div>

  );

}

export default ReviewInfoPanel;