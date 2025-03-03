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
        <div className="container">
          <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <Link href="/" className="d-flex align-items-center mb-2 mb-lg-0 link-body-emphasis text-decoration-none">
              <Image src="/brand/logo.svg" alt="Datarist logo"  className="d-block my-1" />
              <title>Datarist</title>
            </Link>
            <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
              <li><Link href="#" className="nav-link px-2 link-secondary">Overview</Link></li>
              <li><Link href="#" className="nav-link px-2 link-body-emphasis">Inventory</Link></li>
              <li><Link href="#" className="nav-link px-2 link-body-emphasis">Customers</Link></li>
              <li><Link href="#" className="nav-link px-2 link-body-emphasis">Products</Link></li>
            </ul>
            <form className="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
              <input type="search" className="form-control" placeholder="Search..." aria-label="Search">
            </form>
            <div className="dropdown text-end">
              <Link href="#" className="d-block link-body-emphasis text-decoration-none dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                <Image src="https://github.com/mdo.png" alt="mdo" width="32" height="32" className="rounded-circle">
              </Link>
              <ul className="dropdown-menu text-small">
                <li><Link className="dropdown-item" href="#">New project...</Link></li>
                <li><Link className="dropdown-item" href="#">Settings</Link></li>
                <li><Link className="dropdown-item" href="#">Profile</Link></li>
                <li><hr className="dropdown-divider"></li>
                <li><Link className="dropdown-item" href="#">Sign out</Link></li>
              </ul>
            </div>
          </div>
        </div>
      </header>
        <header className="navbar navbar-expand-lg dd-navbar bg-dark ">
          <nav className="container-xxl dd-gutter flex-wrap flex-lg-nowrap bg-dark" aria-label="Main navigation">
            <div className="d-lg-none nav-logo">
              <Link className="navbar-brand p-0 me-0 me-lg-2" href="https://datarist.com/" aria-label="Datarist">
                <Image src="/brand/logo.svg" alt="Datarist logo"  className="d-block my-1" />
                <title>Datarist</title>
              </Link>
            </div>
            <div className="d-flex">
              <div className="dd-search" id="docsearch" data-dd-docs-version="5.3">
              <button className="navbar-toggler d-flex d-lg-none order-3 p-2" type="button" data-bs-toggle="offcanvas" data-bs-target="#ddNavbar" aria-controls="ddNavbar" aria-label="Toggle navigation">
                
              </button>
              </div>
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