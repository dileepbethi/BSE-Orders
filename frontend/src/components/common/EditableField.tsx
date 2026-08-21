type EditableFieldProps = {
  label: string;
  value: string | number;
  editing: boolean;
  onChange: (value: string) => void;
};

function EditableField({
  label,
  value,
  editing,
  onChange,
}: EditableFieldProps) {
  return (
    <div>
      <p className="text-sm text-slate-400">
        {label}
      </p>

      {editing ? (
        <input
          value={value ?? ""}
          onChange={(e) => onChange(e.target.value)}
          className="mt-2 w-full rounded-lg border border-slate-600 bg-slate-800 px-3 py-2 text-white focus:border-blue-500 focus:outline-none"
        />
      ) : (
        <h2 className="mt-1 text-xl font-semibold text-white">
          {value || "-"}
        </h2>
      )}
    </div>
  );
}

export default EditableField;