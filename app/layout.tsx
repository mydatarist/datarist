import "./globals.css";
import Link from "next/link";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Link href="https://datarist.com">Datarist</Link>
        {children}          
        <Link href="/terms/">Terms</Link>
        <Link href="/privacy/">Privacy</Link>
        <Link href="/cookies/">Cookies</Link>
        <Link href="/contact/">Contact</Link> 
      </body>
    </html>
  );
}