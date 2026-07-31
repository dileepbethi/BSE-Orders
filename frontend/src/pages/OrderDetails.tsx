import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import PageHeader from "../components/common/PageHeader";
import EditableField from "../components/common/EditableField";

import {
  getOrderDetails,
  updateOrder,
  getOrderPdfUrl,
} from "../services/orderDetailsService";

import type {
  OrderDetails,
} from "../services/orderDetailsService";

function OrderDetailsPage() {

  const { id } = useParams();

  const pdfUrl =
  id
    ? getOrderPdfUrl(Number(id))
    : "";

  const [order, setOrder] =
    useState<OrderDetails | null>(null);

  const [editedOrder, setEditedOrder] =
    useState<OrderDetails | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [isEditing, setIsEditing] =
    useState(false);

  useEffect(() => {

    if (!id) return;

    async function loadOrder() {

      try {

        const data =
          await getOrderDetails(Number(id));

        setOrder(data);

        setEditedOrder(data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }

    }

    loadOrder();

  }, [id]);

  async function handleSave() {

    if (!id || !editedOrder) return;

    try {

      await updateOrder(
        Number(id),
        editedOrder
      );

      setOrder(editedOrder);

      setIsEditing(false);

      alert("Order updated successfully.");

    } catch (error) {

      console.error(error);

      alert("Failed to update order.");

    }

  }

  if (loading) {

    return (
      <>
        <PageHeader
          title="Order Details"
          subtitle="Loading..."
        />

        <p className="text-slate-400">
          Loading...
        </p>
      </>
    );

  }

  if (!order || !editedOrder) {

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

        {isEditing ? (

          <div className="flex gap-3">

            <button
              onClick={handleSave}
              className="rounded-lg bg-green-600 px-5 py-2 font-medium text-white hover:bg-green-700"
            >
              Save
            </button>

            <button
              onClick={() => {

                setEditedOrder(order);

                setIsEditing(false);

              }}
              className="rounded-lg bg-slate-600 px-5 py-2 font-medium text-white hover:bg-slate-700"
            >
              Cancel
            </button>

          </div>

        ) : (

          <button
            onClick={() => setIsEditing(true)}
            className="rounded-lg bg-blue-600 px-5 py-2 font-medium text-white hover:bg-blue-700"
          >
            Edit
          </button>

        )}

      </div>

      <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">

        <div className="rounded-xl border border-slate-700 bg-slate-900 p-8">

          <EditableField
            label="Company"
            value={editedOrder.company}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                company: value,
              })
            }
          />

          <EditableField
            label="Customer"
            value={editedOrder.customer || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                customer: value,
              })
            }
          />

          <EditableField
            label="Order Value"
            value={editedOrder.order_value || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                order_value: value,
              })
            }
          />

          <EditableField
            label="Awarding Entity"
            value={editedOrder.awarding_entity || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                awarding_entity: value,
              })
            }
          />
          <EditableField
            label="Execution Period"
            value={editedOrder.execution_period || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                execution_period: value,
              })
            }
          />

          <EditableField
            label="Order Type"
            value={editedOrder.order_type || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                order_type: value,
              })
            }
          />

          <EditableField
            label="Domestic / International"
            value={editedOrder.domestic || ""}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                domestic: value,
              })
            }
          />

          <EditableField
            label="Exchange"
            value={editedOrder.exchange}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                exchange: value,
              })
            }
          />

          <EditableField
            label="Confidence Score"
            value={editedOrder.confidence_score}
            editing={isEditing}
            onChange={(value) =>
              setEditedOrder({
                ...editedOrder,
                confidence_score: Number(value),
              })
            }
          />

          <div className="col-span-2">

            <p className="text-sm text-slate-400">
              Project Description
            </p>

            {isEditing ? (

              <textarea
                value={editedOrder.project_description || ""}
                onChange={(e) =>
                  setEditedOrder({
                    ...editedOrder,
                    project_description: e.target.value,
                  })
                }
                rows={5}
                className="mt-2 w-full rounded-lg border border-slate-600 bg-slate-800 p-3 text-white focus:border-blue-500 focus:outline-none"
              />

            ) : (

              <p className="mt-2 leading-7 text-white">
                {editedOrder.project_description || "-"}
              </p>

            )}

          </div>

          <div className="col-span-2">

            <p className="text-sm text-slate-400">
              Source File
            </p>

            <p className="mt-2 break-all text-white">
              {editedOrder.source_file}
            </p>

          </div>
        </div>
        <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">

  <h2 className="mb-4 text-lg font-semibold text-white">
    Original PDF
  </h2>

  <iframe
    src={pdfUrl}
    title="Original PDF"
    className="h-[900px] w-full rounded-lg border border-slate-700"
  />

</div>

      </div>

    </>

  );

}

export default OrderDetailsPage;