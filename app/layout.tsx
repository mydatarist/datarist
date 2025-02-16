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
        <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
          <div className="container">
            <div className="col-md-4 d-flex align-items-center">
              <Link className="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1" href="/">
                <svg className="bi" width="30" height="24"></svg>
              </Link>
              <span className="mb-3 mb-md-0 text-body-secondary">&copy; 2025 Datarist, Inc.</span>
            </div>
            <ul className="nav col-md-4 justify-content-end list-unstyled d-flex">
              <li className="ms-3"><Link className="text-body-secondary" href="/terms/">Terms</Link></li>
              <li className="ms-3"><Link className="text-body-secondary" href="/privacy/">Privacy</Link></li>
              <li className="ms-3"><Link className="text-body-secondary" href="/cookies/">Cookies</Link></li>
              <li className="ms-3"><Link className="text-body-secondary" href="/contact/">Contact</Link></li>               
            </ul>            
          </div>         
        </footer>                
      </body>
    </html>
  );
}