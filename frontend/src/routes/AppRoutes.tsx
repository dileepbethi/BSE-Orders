import { BrowserRouter, Routes, Route } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard";
import OrderDetails from "../pages/OrderDetails";
import Companies from "../pages/Companies";
import ReviewQueue from "../pages/ReviewQueue";
import Parser from "../pages/Parser";
import Analytics from "../pages/Analytics";
import Settings from "../pages/Settings";

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
            path="/companies"
            element={<Companies />}
          />

          <Route
            path="/review"
            element={<ReviewQueue />}
          />

          <Route
            path="/parser"
            element={<Parser />}
          />

          <Route
            path="/analytics"
            element={<Analytics />}
          />

          <Route
            path="/settings"
            element={<Settings />}
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