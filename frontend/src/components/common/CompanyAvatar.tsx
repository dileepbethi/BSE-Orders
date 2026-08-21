type Props = {
  company: string;
};

function CompanyAvatar({
  company,
}: Props) {

  const initials = company
    .split(" ")
    .map((word) => word[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();

  return (

    <div
      className="
        flex
        h-10
        w-10
        items-center
        justify-center
        rounded-full
        bg-blue-600
        font-semibold
        text-white
      "
    >
      {initials}
    </div>

  );

}

export default CompanyAvatar;