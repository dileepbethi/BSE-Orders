import { NavLink } from "react-router-dom";

const menu = [

  {
    title: "Dashboard",
    path: "/",
    icon: "📊",
  },

  {
    title: "Orders",
    path: "/orders",
    icon: "📄",
  },

  {
    title: "Companies",
    path: "/companies",
    icon: "🏢",
  },

  {
    title: "Review Queue",
    path: "/review",
    icon: "✅",
  },

  {
    title: "Parser",
    path: "/parser",
    icon: "🤖",
  },

  {
    title: "Analytics",
    path: "/analytics",
    icon: "📈",
  },

  {
    title: "Settings",
    path: "/settings",
    icon: "⚙️",
  },

];

function Sidebar() {

  return (

    <aside
      className="
        fixed
        left-0
        top-0
        z-40
        flex
        h-screen
        w-64
        flex-col
        border-r
        border-slate-800
        bg-slate-950
      "
    >

      <div className="border-b border-slate-800 p-6">

        <h1 className="text-2xl font-bold text-white">

          OrderIQ

        </h1>

        <p className="mt-1 text-xs text-slate-400">

          Procurement Intelligence

        </p>

      </div>

      <nav className="flex-1 space-y-2 p-4">

        {menu.map((item) => (

          <NavLink
            key={item.title}
            to={item.path}
            className={({ isActive }) =>

              `flex items-center gap-3 rounded-xl px-4 py-3 transition-all ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`

            }
          >

            <span>{item.icon}</span>

            <span>{item.title}</span>

          </NavLink>

        ))}

      </nav>

    </aside>

  );

}

export default Sidebar;