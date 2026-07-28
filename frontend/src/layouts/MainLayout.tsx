import { Outlet } from "react-router-dom";
import Sidebar from "../components/navigation/Sidebar";
import TopHeader from "../components/navigation/TopHeader";

function MainLayout() {
  return (
    <div className="flex min-h-screen">
      <Sidebar />

      <main className="flex flex-1 flex-col">
        <TopHeader />

        <div className="flex-1 p-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
}

export default MainLayout;