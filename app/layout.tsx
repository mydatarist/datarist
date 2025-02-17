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
          <div className="container-fluid">
            <div className="col-md-6 justify-content-start list-unstyled d-flex">
              <ul className="nav">
                <li className="text-body-secondary"><Link className="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1" href="/"><svg width="30" height="24"></svg></Link> &copy; 2025 Datarist, Inc.</li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/terms/">Terms</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/privacy/">Privacy</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/cookies/">Cookies</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/contact/">Contact</Link></li>               
              </ul>
            </div>
            <div className="col-md-6 justify-content-end list-unstyled d-flex">
              <ul className="nav">
                <li className="text-body-secondary"><Link className="text-body-secondary text-decoration-none" href="/"><svg width="30" height="24"></svg></Link> &copy; 2025 Datarist, Inc.</li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/terms/">Terms</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/privacy/">Privacy</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/cookies/">Cookies</Link></li>
                <li className="ms-3"><Link className="text-body-secondary text-decoration-none" href="/contact/">Contact</Link></li>               
              </ul>
            </div>             
          </div>  
        </footer>                                
      </body>
    </html>
  );
}