import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Card from "../ui/Card";

import {
  getOrders,
  searchOrders,
} from "../../services/ordersService";

import type { Order } from "../../services/ordersService";

function OrdersTable() {

  const [orders, setOrders] = useState<Order[]>([]);
  const [search, setSearch] = useState("");

  const navigate = useNavigate();

  useEffect(() => {

    async function load() {

      try {

        if (search.trim() === "") {

          const data = await getOrders(1, 10);
          setOrders(data.items);

        } else {

          const data = await searchOrders(search);
          setOrders(data);

        }

      } catch (error) {

        console.error(error);

      }

    }

    load();

  }, [search]);

  return (

    <Card>

      <div className="mb-4 flex items-center justify-between">

        <h2 className="text-xl font-bold text-white">
          Latest Orders
        </h2>

        <input
          type="text"
          placeholder="Search company or customer..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-72 rounded-lg border border-slate-700 bg-slate-800 px-4 py-2 text-white outline-none"
        />

      </div>

      <div className="overflow-x-auto">

        <table className="min-w-full text-sm">

          <thead>

            <tr className="border-b border-slate-700">

              <th className="p-3 text-left">
                Company
              </th>

              <th className="p-3 text-left">
                Customer
              </th>

              <th className="p-3 text-left">
                Date
              </th>

              <th className="p-3 text-left">
                Value
              </th>

            </tr>

          </thead>

          <tbody>

            {orders.map((order) => (

              <tr
                key={order.id}
                onClick={() => navigate(`/order/${order.id}`)}
                className="cursor-pointer border-b border-slate-800 transition hover:bg-slate-800"
              >

                <td className="p-3">
                  {order.company}
                </td>

                <td className="p-3">
                  {order.customer || "-"}
                </td>

                <td className="p-3">
                  {order.announcement_date}
                </td>

                <td className="p-3">
                  {order.order_value || "-"}
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