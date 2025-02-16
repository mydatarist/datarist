import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./app.css";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Datarist: Data Insights.",
  description: "Empowering people and organizations with data.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Link href="https://datarist.com">Datarist</Link>
        <Link href="/solutions/">Solutions</Link>
        <Link href="/pricing/">Pricing</Link>
        {children}        
        <Link href="/about/">About</Link>        
        <Link href="/terms/">Terms</Link>
        <Link href="/privacy/">Privacy</Link>
        <Link href="/cookies/">Cookies</Link>
        <Link href="/contact/">Contact</Link>      
      </body>
    </html>
  );
}
