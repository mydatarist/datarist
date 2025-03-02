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
        <header className="navbar navbar-expand-lg dd-navbar bg-dark sticky-top">
          <nav className="container-xxl dd-gutter flex-wrap flex-lg-nowrap bg-dark" aria-label="Main navigation">
            <div className="d-lg-none nav-logo">
              <Link className="navbar-brand p-0 me-0 me-lg-2" href="https://datarist.com/" aria-label="Datarist">
                <Image src="/brand/logo.svg" alt="Datarist logo"  className="d-block my-1" />
                <title>Datarist</title>
              </Link>
            </div>
            <div className="d-flex">
              <div className="dd-search" id="docsearch" data-dd-docs-version="5.3">
              
            </div>
          </nav>
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