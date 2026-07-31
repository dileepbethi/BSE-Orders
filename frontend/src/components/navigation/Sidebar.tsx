import { NavLink } from "react-router-dom";

const menuItems = [
  {
    name: "Dashboard",
    path: "/",
    icon: "📊",
  },
  {
    name: "Orders",
    path: "/",
    icon: "📄",
  },
  {
    name: "Companies",
    path: "/companies",
    icon: "🏢",
  },
  {
    name: "Review Queue",
    path: "/review",
    icon: "✅",
  },
  {
    name: "Parser",
    path: "/parser",
    icon: "🤖",
  },
  {
    name: "Analytics",
    path: "/analytics",
    icon: "📈",
  },
  {
    name: "Settings",
    path: "/settings",
    icon: "⚙️",
  },
];

function Sidebar() {
  return (
    <aside className="flex h-screen w-72 flex-col border-r border-slate-800 bg-slate-950">
      <div className="border-b border-slate-800 p-6">
        <h1 className="text-2xl font-bold text-white">
          OrderIQ
        </h1>

        <p className="mt-2 text-sm text-slate-400">
          Enterprise Procurement Intelligence
        </p>
      </div>

      <nav className="flex-1 space-y-2 p-4">
        {menuItems.map((item) => (
          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 rounded-xl px-4 py-3 font-medium transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            <span className="text-lg">{item.icon}</span>
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>

      <div className="border-t border-slate-800 p-5">
        <div className="rounded-xl bg-slate-900 p-4">
          <p className="text-xs uppercase tracking-wider text-slate-500">
            Parser Status
          </p>

          <div className="mt-2 flex items-center gap-2">
            <div className="h-2 w-2 rounded-full bg-emerald-500"></div>

            <span className="text-sm text-emerald-400">
              Running
            </span>
          </div>
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;