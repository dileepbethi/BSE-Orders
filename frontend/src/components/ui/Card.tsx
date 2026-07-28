import type { ReactNode } from "react";

type CardProps = {
  children: ReactNode;
};

function Card({ children }: CardProps) {
  return (
    <div className="rounded-xl border border-slate-700 bg-slate-800 p-6">
      {children}
    </div>
  );
}

export default Card;