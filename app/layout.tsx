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
        <footer className="d-flex flex-wrap py-3 my-4 border-top">
          <div className="container">
            <ul className="nav list-unstyled d-flex">
              <li className="text-body-secondary"><Link className="text-body-secondary" href="/"><svg className="bi" width="30" height="24"></svg></Link>&copy; 2025 Datarist, Inc.</li>
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