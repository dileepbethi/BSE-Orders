import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import OrderDetails from "../pages/OrderDetails";

function AppRoutes() {
  return (
    <BrowserRouter>

      <Routes>

        <Route element={<MainLayout />}>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/order/:id"
            element={<OrderDetails />}
          />

        </Route>

      </Routes>

    </BrowserRouter>
  );
}

export default AppRoutes;