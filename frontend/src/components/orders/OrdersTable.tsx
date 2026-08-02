import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Card from "../ui/Card";

import {
  getOrders,
  searchOrders,
} from "../../services/ordersService";

import type { Order } from "../../types/order";

type Props = {
  page: number;
  setPages: React.Dispatch<React.SetStateAction<number>>;
};

function OrdersTable({
  page,
  setPages,
}: Props) {

  const [orders, setOrders] = useState<Order[]>([]);
  const [search, setSearch] = useState("");

  const navigate = useNavigate();

  useEffect(() => {

    async function loadOrders() {

      try {

        if (search.trim() === "") {

          const response = await getOrders(page, 20);

          console.log(response);

          setOrders(response.items);

          setPages(response.pages);

        } else {

          const response = await searchOrders(search);

          setOrders(response);

          setPages(1);

        }

      } catch (error) {

        console.error(error);

      }

    }

    loadOrders();

  }, [page, search, setPages]);

  return (

    <Card>

      <div className="mb-5 flex items-center justify-between">

        <h2 className="text-xl font-semibold text-white">
          Enterprise Orders
        </h2>

        <input
          type="text"
          placeholder="Search company or customer..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-80 rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-white outline-none"
        />

      </div>

      <div className="overflow-x-auto">

        <table className="min-w-full">

          <thead>

            <tr className="border-b border-slate-700 text-left text-sm text-slate-400">

              <th className="p-4">Company</th>
              <th className="p-4">Customer</th>
              <th className="p-4">Exchange</th>
              <th className="p-4">Value</th>
              <th className="p-4">Date</th>
              <th className="p-4">Status</th>
              <th className="p-4">Actions</th>

            </tr>

          </thead>

          <tbody>

            {orders.map((order) => (

              <tr
                key={order.id}
                className="border-b border-slate-800 hover:bg-slate-800/60"
              >

                <td className="p-4 text-white">
                  {order.company}
                </td>

                <td className="p-4 text-slate-300">
                  {order.customer || "-"}
                </td>

                <td className="p-4">
                  <span className="rounded-full bg-slate-800 px-3 py-1 text-xs text-white">
                    {order.exchange}
                  </span>
                </td>

                <td className="p-4 text-emerald-400">
                  {order.order_value || "-"}
                </td>

                <td className="p-4 text-slate-300">
                  {order.announcement_date}
                </td>

                <td className="p-4">
                  <span className="rounded-full bg-emerald-600 px-3 py-1 text-xs text-white">
                    {order.processing_status}
                  </span>
                </td>

                <td className="p-4">

                  <button
                    onClick={() => navigate(`/order/${order.id}`)}
                    className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
                  >
                    View
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

export default OrdersTable;