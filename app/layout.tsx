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
        <div className="container">
          <footer className="py-5">
            <div className="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
              <p>2025 Datarist, Inc.</p>
              <ul className="list-unstyled d-flex">
                <li className="ms-3"><Link class="link-body-emphasis" href="/terms/">Terms</Link></li>
                <li className="ms-3"><Link class="link-body-emphasis" href="/privacy/">Privacy</Link></li>
                <li className="ms-3"><Link class="link-body-emphasis" href="/cookies/">Cookies</Link></li>
                <li className="ms-3"><Link class="link-body-emphasis" href="/contact/">Contact</Link></li>
              </ul>
            </div>
          </footer>
        </div>     
      </body>
    </html>
  );
}
