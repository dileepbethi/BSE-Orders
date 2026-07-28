function Sidebar() {
  return (
    <aside
      style={{
        width: "250px",
        background: "#111827",
        color: "white",
        padding: "20px",
      }}
    >
      <h2>OrderIQ</h2>

      <hr />

      <p>📊 Dashboard</p>
      <p>🏢 Companies</p>
      <p>📄 Review</p>
      <p>⚙️ Parser</p>
      <p>⚡ Settings</p>
    </aside>
  );
}

export default Sidebar;