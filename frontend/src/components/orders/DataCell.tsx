type Props = {
  date: string;
};

function DateCell({ date }: Props) {
  return (
    <span className="text-slate-300">
      {date}
    </span>
  );
}

export default DateCell;