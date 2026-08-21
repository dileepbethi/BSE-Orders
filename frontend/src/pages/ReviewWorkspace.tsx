import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

import PageHeader from "../components/common/PageHeader";

import ReviewPdfViewer from "../components/review/ReviewPdfViewer";
import ReviewInfoPanel from "../components/review/ReviewInfoPanel";
import ReviewActions from "../components/review/ReviewActions";

import {
  getReview,
  type Review,
} from "../services/reviewService";

function ReviewWorkspace() {

  const [searchParams] = useSearchParams();

  const id = Number(searchParams.get("id"));

  const [review, setReview] = useState<Review | null>(null);

  useEffect(() => {

    async function loadReview() {

      try {

        const data = await getReview(id);

        setReview(data);

      } catch (error) {

        console.error(error);

      }

    }

    if (id) {

      loadReview();

    }

  }, [id]);

  if (!review) {

    return (
      <div className="p-10 text-white">
        Loading...
      </div>
    );

  }

  return (

    <>

      <PageHeader
        title="Review Workspace"
        subtitle="Human Validation"
      />

      <div className="mb-6 rounded-2xl border border-slate-800 bg-slate-900 p-6">

        <div className="flex items-center justify-between">

          <div>

            <h1 className="text-3xl font-bold text-white">

              {review.company}

            </h1>

            <p className="mt-2 text-slate-400">

              AI extracted procurement announcement

            </p>

          </div>

          <span className="rounded-full bg-yellow-500/20 px-5 py-2 font-semibold text-yellow-400">

            Confidence {review.confidence_score}%

          </span>

        </div>

      </div>

      <div className="grid grid-cols-2 gap-6">

        <ReviewPdfViewer />

       <ReviewInfoPanel review={review} />

      </div>

      <ReviewActions />

    </>

  );

}

export default ReviewWorkspace;