import { Eye } from "lucide-react";

type Props = {
  onView: () => void;
};

function ActionButtons({
  onView,
}: Props) {
  return (
    <button
      onClick={onView}
      className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-blue-700"
    >
      <Eye size={16} />
      View
    </button>
  );
}

export default ActionButtons;