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
              <Image src="/brand/logo.svg" alt="Datarist logo"  className="bi me-2" width="38" height="30" aria-label="Datarist"/>
              <title>Datarist</title>
            </Link>
            <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
              <li><Link href="/products/" className="nav-link px-2 link-body-emphasis">Products</Link></li>
              <li><Link href="/solutions/" className="nav-link px-2 link-body-emphasis">Solutions</Link></li>
            </ul>
            <div className="text-end">
              <Link href="https://datarist.com/"><button type="button" className="btn btn-light me-2">Sign in</button></Link>
              <Link href="https://datarist.com/"><button type="button" className="btn btn-outline-dark">Sign up</button></Link>
            </div>
          </div>
        </header> 
        {children} 
        <footer className="py-3 my-4 border-top footer text-body-secondary">
          <div className="container-fluid">
            <ul className="nav">
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