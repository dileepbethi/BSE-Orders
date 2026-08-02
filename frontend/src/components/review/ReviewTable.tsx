import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Card from "../ui/Card";

import {
  getPendingReviews,
  type Review,
} from "../../services/reviewService";

function ReviewTable() {

  const [reviews, setReviews] = useState<Review[]>([]);

  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {

    async function loadReviews() {

      try {

        const data =
          await getPendingReviews();

        setReviews(data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }

    }

    loadReviews();

  }, []);

  if (loading) {

    return (

      <Card>

        <p className="text-slate-400">
          Loading reviews...
        </p>

      </Card>

    );

  }

  return (

    <Card>

      <div className="mb-5">

        <h2 className="text-xl font-semibold text-white">
          Pending Reviews
        </h2>

      </div>

      <div className="overflow-x-auto">

        <table className="min-w-full">

          <thead>

            <tr className="border-b border-slate-700 text-left text-sm text-slate-400">

              <th className="p-4">Company</th>
              <th className="p-4">Customer</th>
              <th className="p-4">Exchange</th>
              <th className="p-4">Confidence</th>
              <th className="p-4">Action</th>

            </tr>

          </thead>

          <tbody>

            {reviews.map((review) => (

              <tr
                key={review.id}
                className="border-b border-slate-800 hover:bg-slate-800/60"
              >

                <td className="p-4 text-white">
                  {review.company}
                </td>

                <td className="p-4 text-slate-300">
                  {review.customer || "-"}
                </td>

                <td className="p-4 text-slate-300">
                  {review.exchange}
                </td>

                <td className="p-4">

                  <span className="rounded-full bg-yellow-500/20 px-3 py-1 text-xs font-semibold text-yellow-400">

                    {review.confidence_score}%

                  </span>

                </td>

                <td className="p-4">

                  <button
                    onClick={() =>
                      navigate(`/review/workspace?id=${review.id}`)
                    }
                    className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
                  >

                    Review

                  </button>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </Card>

  );

}

export default ReviewTable;