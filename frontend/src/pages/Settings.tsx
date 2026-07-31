import PageHeader from "../components/common/PageHeader";

function Settings() {
  return (
    <>
      <PageHeader
        title="Settings"
        subtitle="Application Configuration"
      />

      <div className="rounded-xl border border-slate-700 bg-slate-900 p-10">

        <h2 className="text-2xl font-semibold text-white">
          Settings
        </h2>

        <p className="mt-3 text-slate-400">
          User preferences, parser configuration and system settings will be
          managed here.
        </p>

      </div>
    </>
  );
}

export default Settings;