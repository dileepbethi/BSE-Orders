type Props = {
  pdfUrl: string;
};

function PdfToolbar({
  pdfUrl,
}: Props) {
  return (
    <div className="mb-4 flex gap-3">

      <a
        href={pdfUrl}
        target="_blank"
        rel="noreferrer"
        className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
      >
        Open PDF
      </a>

      <a
        href={pdfUrl}
        download
        className="rounded-lg bg-slate-700 px-4 py-2 text-white hover:bg-slate-600"
      >
        Download
      </a>

    </div>
  );
}

export default PdfToolbar;