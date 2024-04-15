import Image from "next/image";

type ButtonProps={
    type: "button" | 'submit';
    title: string;
    icon?: string;
    variant: string;
}

export default function Button({ type, icon, title, variant}: ButtonProps) {
  return (
    <button type={type} className={`flexCenter gap-3 rounded-full border ${variant}`}>
          {icon && <Image src={icon} alt={title} height={24} width={24} /> }
          <label className=" bold-16 whitespace-normal">
            {title}
          </label>
    </button>
  )
}
