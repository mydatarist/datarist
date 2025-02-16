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
        <div className="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
          <Link className="nav-link p-0 text-body-secondary" href="/terms/">Terms</Link>
          <Link className="nav-link p-0 text-body-secondary" href="/privacy/">Privacy</Link>
          <Link className="nav-link p-0 text-body-secondary" href="/cookies/">Cookies</Link>
          <Link className="nav-link p-0 text-body-secondary" href="/contact/">Contact</Link> 
        </div>        
      </body>
    </html>
  );
}