import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import PageHeader from "../components/common/PageHeader";
import EditableField from "../components/common/EditableField";

import SectionCard from "../components/orderDetails/SectionCard";
import InfoRow from "../components/orderDetails/InfoRow";
import StatusBadge from "../components/orderDetails/StatusBadge";
import PdfToolbar from "../components/orderDetails/PdfToolbar";

import {
  getOrderDetails,
  updateOrder,
  getOrderPdfUrl,
} from "../services/orderDetailsService";

import type { OrderDetails } from "../services/orderDetailsService";

function OrderDetailsPage() {
  const { id } = useParams();

  const pdfUrl = id ? getOrderPdfUrl(Number(id)) : "";

  const [order, setOrder] = useState<OrderDetails | null>(null);
  const [editedOrder, setEditedOrder] = useState<OrderDetails | null>(null);

  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);

  const [reviewNotes, setReviewNotes] = useState("");

  useEffect(() => {
    if (!id) return;

    async function loadOrder() {
      try {
        const data = await getOrderDetails(Number(id));

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
    if (!editedOrder || !id) return;

    try {
      await updateOrder(Number(id), editedOrder);

      setOrder(editedOrder);

      setIsEditing(false);

      alert("Saved successfully.");
    } catch (error) {
      console.error(error);
      alert("Unable to save.");
    }
  }

  if (loading) {
    return (
      <>
        <PageHeader
          title="Order Details"
          subtitle="Loading..."
        />
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
      </>
    );
  }

  return (
    <>
      <PageHeader
        title={editedOrder.company}
        subtitle="Enterprise Order Review Workspace"
      />

      <div className="mb-6 flex items-center justify-between">

        <StatusBadge
          status={editedOrder.processing_status}
        />

        <div className="flex gap-3">

          {isEditing ? (
            <>
              <button
                onClick={handleSave}
                className="rounded-lg bg-emerald-600 px-5 py-2 font-medium text-white hover:bg-emerald-700"
              >
                Save
              </button>

              <button
                onClick={() => {
                  setEditedOrder(order);
                  setIsEditing(false);
                }}
                className="rounded-lg bg-slate-700 px-5 py-2 text-white"
              >
                Cancel
              </button>
            </>
          ) : (
            <button
              onClick={() => setIsEditing(true)}
              className="rounded-lg bg-blue-600 px-5 py-2 text-white hover:bg-blue-700"
            >
              Edit
            </button>
          )}

        </div>

      </div>

      <div className="grid gap-6 xl:grid-cols-2">

        <SectionCard title="Order Information">

          <InfoRow
            label="Company"
            value={editedOrder.company}
          />

          <InfoRow
            label="Customer"
            value={
              <EditableField
                label=""
                value={editedOrder.customer || ""}
                editing={isEditing}
                onChange={(value) =>
                  setEditedOrder({
                    ...editedOrder,
                    customer: value,
                  })
                }
              />
            }
          />

          <InfoRow
            label="Order Value"
            value={
              <span className="rounded-full bg-emerald-600 px-3 py-1 text-white">
                {editedOrder.order_value || "-"}
              </span>
            }
          />

          <InfoRow
            label="Awarding Entity"
            value={editedOrder.awarding_entity || "-"}
          />

          <InfoRow
            label="Execution"
            value={editedOrder.execution_period || "-"}
          />

          <InfoRow
            label="Exchange"
            value={editedOrder.exchange}
          />

          <InfoRow
            label="Confidence"
            value={`${editedOrder.confidence_score}%`}
          />

          <div className="mt-6">

            <h3 className="mb-2 text-sm text-slate-400">
              Project Description
            </h3>

            {isEditing ? (
              <textarea
                rows={6}
                value={editedOrder.project_description || ""}
                onChange={(e) =>
                  setEditedOrder({
                    ...editedOrder,
                    project_description: e.target.value,
                  })
                }
                className="w-full rounded-lg border border-slate-700 bg-slate-800 p-4 text-white"
              />
            ) : (
              <div className="rounded-lg bg-slate-800 p-4 leading-7 text-white">
                {editedOrder.project_description || "-"}
              </div>
            )}

          </div>

          <div className="mt-6">

            <h3 className="mb-2 text-sm text-slate-400">
              Review Notes
            </h3>

            <textarea
              rows={5}
              value={reviewNotes}
              onChange={(e) => setReviewNotes(e.target.value)}
              placeholder="Add analyst notes..."
              className="w-full rounded-lg border border-slate-700 bg-slate-800 p-4 text-white"
            />

          </div>

        </SectionCard>

        <SectionCard title="Original Announcement PDF">

          <PdfToolbar pdfUrl={pdfUrl} />

          <p className="mb-2 text-xs text-slate-500">
              {pdfUrl}
          </p>

          <>
              <p className="mb-2 text-xs text-slate-500">
                 {pdfUrl}
              </p>

            <iframe
                src={pdfUrl}
                title="Original PDF"
                loading="lazy"
                className="h-[900px] w-full rounded-xl bg-white"
              />
          </>

        </SectionCard>

      </div>
    </>
  );
}

export default OrderDetailsPage;