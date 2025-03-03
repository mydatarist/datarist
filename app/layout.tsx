import Script from "next/script";
import "./globals.css";
import Link from "next/link";
import Image from "next/image";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
      </head>
      <body> 
        <header className="p-3 mb-3 border-bottom">
          <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <Link href="https://datarist.com/" className="d-flex align-items-center mb-2 mb-lg-0 link-body-emphasis text-decoration-none">
              <Image src="/brand/logo.svg" alt="Datarist logo"  className="d-block my-1" />
              <title>Datarist</title>
            </Link>
            <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
              <li><Link href="/terms/" className="nav-link px-2 link-secondary">Terms</Link></li>
              <li><Link href="/privacy/" className="nav-link px-2 link-body-emphasis">Privacy</Link></li>
              <li><Link href="/cookies/" className="nav-link px-2 link-body-emphasis">Cookies</Link></li>
              <li><Link href="/contact/" className="nav-link px-2 link-body-emphasis">Contact</Link></li>
            </ul>
          </div>
        </header>      
        <Link href="https://datarist.com">Datarist</Link>
        {children} 
        <footer className="py-3 my-4 border-top footer text-body-secondary">
          <div className="container-fluid">
            <ul className="nav">
              <li className="text-body-secondary"><Link className="text-body-secondary text-decoration-none" href="/"><Image src="/brand/logo.svg" alt="Datarist logo" width="20" height="16" /></Link></li>
              <li className="ms-1 text-body-secondary">&copy; 2025 Datarist, Inc.</li>
              <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/terms/">Terms</Link></li>
              <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/privacy/">Privacy</Link></li>
              <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/cookies/">Cookies</Link></li>
              <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/contact/">Contact</Link></li>               
            </ul>        
          </div>  
        </footer>                                
      </body>
    </html>
  );
}