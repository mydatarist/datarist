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
        <div class="container">
          <footer class="py-5">
            <div class="d-flex flex-column flex-sm-row justify-content-between py-4 my-4 border-top">
              <p>&copy; 2024 Company, Inc. All rights reserved.</p>
              <ul class="list-unstyled d-flex">
                <li class="ms-3"><a class="link-body-emphasis" href="#"></a></li>
                <li class="ms-3"><a class="link-body-emphasis" href="#"></a></li>
                <li class="ms-3"><a class="link-body-emphasis" href="#"></a></li>
              </ul>
            </div>
          </footer>
        </div>     
      </body>
    </html>
  );
}
