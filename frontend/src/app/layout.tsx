import type { Metadata } from "next";
// import { ClerkProvider } from '@clerk/nextjs'
import { Inter } from "next/font/google";
import "./globals.css";
import { Navbar } from "@/components/Navbar";
import Footer from "@/components/Footer";


const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Asadbek",
  description: "Ul/Ux",
};

export default function RootLayout({ children, }: Readonly<{ children: React.ReactNode; }>) {
  return (
    // <ClerkProvider>
      <html lang="en">
        <body>
          < Navbar />
           <main className="relative overflow-hidden">
           {children}
           </main>
          < Footer />
          </body>
      </html>
    // </ClerkProvider>
  );
}
