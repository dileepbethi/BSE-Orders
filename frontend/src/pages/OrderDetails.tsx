import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import PageHeader from "../components/common/PageHeader";

import {
  getOrderDetails,
} from "../services/orderDetailsService";

import type {
  OrderDetails,
} from "../services/orderDetailsService";

function OrderDetailsPage() {

  const { id } = useParams();

  const [order, setOrder] = useState<OrderDetails | null>(null);

  useEffect(() => {

    if (!id) return;

    getOrderDetails(Number(id))
      .then(setOrder)
      .catch((error) => {
        console.error("Order Details API Error:", error);
      });

  }, [id]);

  if (!order) {

    return (
      <>
        <PageHeader
          title="Order Details"
          subtitle="Loading..."
        />

        <p className="text-slate-400">
          Loading order...
        </p>
      </>
    );

  }

  return (

    <>
      <PageHeader
        title="Order Details"
        subtitle="Corporate Announcement"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-8">

        <div className="grid grid-cols-2 gap-6">

          <div>
            <p className="text-sm text-slate-400">
              Company
            </p>

            <h2 className="mt-1 text-xl font-semibold text-white">
              {order.company}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Customer
            </p>

            <h2 className="mt-1 text-xl font-semibold text-white">
              {order.customer || "-"}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Announcement Date
            </p>

            <h2 className="mt-1 text-xl font-semibold text-white">
              {order.announcement_date}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Order Value
            </p>

            <h2 className="mt-1 text-xl font-semibold text-green-400">
              {order.order_value || "-"}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Exchange
            </p>

            <h2 className="mt-1 text-xl font-semibold text-white">
              {order.exchange}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Processing Status
            </p>

            <h2 className="mt-1 text-xl font-semibold text-emerald-400">
              {order.processing_status}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Confidence Score
            </p>

            <h2 className="mt-1 text-xl font-semibold text-white">
              {order.confidence_score}
            </h2>
          </div>

          <div>
            <p className="text-sm text-slate-400">
              Source File
            </p>

            <h2 className="mt-1 break-all text-sm text-white">
              {order.source_file}
            </h2>
          </div>

        </div>

      </div>

    </>

  );

}

export default OrderDetailsPage;