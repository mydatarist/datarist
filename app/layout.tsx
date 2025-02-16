import type { Metadata } from "next";
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
      <body className={inter.className}>{children}
        <Link href="/contact/">Contact</Link>
      </body>
    </html>
  );
}
