import { useState } from "react";

import PageHeader from "../components/common/PageHeader";

import OrdersToolbar from "../components/orders/OrdersToolbar";
import OrdersFilters from "../components/orders/OrdersFilters";
import OrdersTable from "../components/orders/OrdersTable";
import OrdersPagination from "../components/orders/OrdersPagination";

function Orders() {

  const [page, setPage] = useState(1);

  const [pages, setPages] = useState(1);

  return (

    <>

      <PageHeader
        title="Orders"
        subtitle="Enterprise Procurement Orders"
      />

      <OrdersToolbar />

      <div className="mt-6">
        <OrdersFilters />
      </div>

      <div className="mt-6">

        <OrdersTable
          page={page}
          setPages={setPages}
        />

      </div>

      <div className="mt-6">

        <OrdersPagination
          page={page}
          pages={pages}
          onPageChange={setPage}
        />

      </div>

    </>

  );

}

export default Orders;