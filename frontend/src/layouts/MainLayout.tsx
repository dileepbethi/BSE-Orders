import { Outlet } from "react-router-dom";

import Sidebar from "../components/navigation/Sidebar";
import TopHeader from "../components/navigation/TopHeader";

function MainLayout() {

  return (

    <div className="bg-slate-950">

      <Sidebar />

      <main className="ml-64 min-h-screen">

        <TopHeader />

        <div
          className="
            h-[calc(100vh-64px)]
            overflow-y-auto
            p-8
          "
        >
          <Outlet />
        </div>

      </main>

    </div>

  );

}

export default MainLayout;