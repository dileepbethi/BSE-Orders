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

  const [order, setOrder] =
    useState<OrderDetails | null>(null);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    if (!id) return;

    async function loadOrder() {

      try {

        const data = await getOrderDetails(Number(id));

        setOrder(data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }

    }

    loadOrder();

  }, [id]);

  if (loading) {

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

  if (!order) {

    return (
      <>
        <PageHeader
          title="Order Details"
          subtitle="Not Found"
        />

        <p className="text-red-400">
          Order not found.
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

    <div className="mb-6 flex justify-end">

      <button
        className="rounded-lg bg-blue-600 px-5 py-2 font-medium text-white hover:bg-blue-700"
      >
        Edit
      </button>

    </div>

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
    Order Value (Crore)
  </p>

  <h2 className="mt-1 text-xl font-semibold text-green-400">
    {order.order_value_crore ?? "-"}
  </h2>
</div>

<div>
  <p className="text-sm text-slate-400">
    Awarding Entity
  </p>

  <h2 className="mt-1 text-xl font-semibold text-white">
    {order.awarding_entity || "-"}
  </h2>
</div>

<div>
  <p className="text-sm text-slate-400">
    Execution Period
  </p>

  <h2 className="mt-1 text-xl font-semibold text-white">
    {order.execution_period || "-"}
  </h2>
</div>

<div>
  <p className="text-sm text-slate-400">
    Order Type
  </p>

  <h2 className="mt-1 text-xl font-semibold text-white">
    {order.order_type || "-"}
  </h2>
</div>
<div>
  <p className="text-sm text-slate-400">
    Domestic / International
  </p>

  <h2 className="mt-1 text-xl font-semibold text-white">
    {order.domestic || "-"}
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

<div className="col-span-2">
  <p className="text-sm text-slate-400">
    Project Description
  </p>

  <p className="mt-2 leading-7 text-white">
    {order.project_description || "-"}
  </p>
</div>

<div className="col-span-2">
  <p className="text-sm text-slate-400">
    Source File
  </p>

  <p className="mt-2 break-all text-white">
    {order.source_file}
  </p>
</div>
</div>
    </div>

  </>

);

}

export default OrderDetailsPage;