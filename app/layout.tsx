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
    <html lang="en" data-bs-theme="light">
      <!-- Google tag (gtag.js) -->
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-TBTRB5K1Q9"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-TBTRB5K1Q9');
      </script>
      <body className={inter.className}>{children}
        <Link href="/contact/">Contact</Link>
      </body>
    </html>
  );
}
