import Camp from "@/components/Camp";
import Features from "@/components/Features";
import GetApp from "@/components/GetApp";
import Gudie from "@/components/Gudie";
import Hero from "@/components/Hero";
import Image from "next/image";


export default function Home() {
  return (
      <>
        < Hero />
        < Camp />
        < Gudie />
        < Features />
        < GetApp />
      </>
  );
}
