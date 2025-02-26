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
        <Script src={'https://www.googletagmanager.com/gtag/js?id=G-RS1PX7109Y'} strategy="afterInteractive" />
        <Script id="google-analytics" strategy="afterInteractive">
          {"window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);}"}
        </Script>
        <Script src={`https://www.googletagmanager.com/gtag/js?id=G-RS1PX7109Y`} strategy="afterInteractive" />
        <Script id='google-analytics' strategy="afterInteractive">
        {
          ` window.dataLayer = window.dataLayer || []; 
            function gtag(){dataLayer.push(arguments);} 
            gtag('js', new Date()); 
            gtag('config', 'G-RS1PX7109Y');
          `
        }
        </Script> 
      </head>
      <body>
        <header className="navbar navbar-expand-lg dd-navbar bg-dark sticky-top">
          <nav className="container-xxl dd-gutter flex-wrap flex-lg-nowrap bg-dark" aria-label="Main navigation">
            <div className="d-lg-none" style="width: 4.25rem;"></div>
              <a className="navbar-brand p-0 me-0 me-lg-2" href="https://datarist.com/" aria-label="Datarist">
                <Image src="/brand/logo.svg" alt="Datarist logo"  className="d-block my-1"  role="img" alt="Datarist" />
                <title>Datarist</title>
              </a>
            <div className="d-flex">
              <div className="dd-search" id="docsearch" data-dd-docs-version="5.3"></div>
              <button className="navbar-toggler d-flex d-lg-none order-3 p-2" type="button" data-bs-toggle="offcanvas" data-bs-target="#ddNavbar" aria-controls="ddNavbar" aria-label="Toggle navigation">
                <svg className="bi" aria-hidden="true"><use xlink:href="#three-dots"></use></svg>
              </button>
            </div>
            <div className="offcanvas-lg offcanvas-end flex-grow-1 bg-dark" tabindex="-1" id="ddNavbar" aria-labelledby="ddNavbarOffcanvasLabel" data-bs-scroll="true">
              <div className="offcanvas-header px-4 pb-0">
                <h5 className="offcanvas-title text-white" id="ddNavbarOffcanvasLabel"><a class="nav-link px-0" href="https://datarist.com"><img src="https://datarist.com/assets/brand/logo-white.png"  role="img" alt="Datarist" /></a></h5>
                <button type="button" className="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close" data-bs-target="#ddNavbar"></button>
              </div>
              <div className="offcanvas-body p-4 pt-0 p-lg-0">
                <hr className="d-lg-none text-white-50">
                <ul className="navbar-nav flex-row flex-wrap dd-navbar-nav">
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" aria-current="true" href="https://datarist.com/solutions/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Solutions');">Solutions</a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" aria-current="true" href="https://datarist.com/catalog/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Catalog');">Catalog</a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" aria-current="true" href="https://datarist.com/publish/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Publish');">Publish</a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" aria-current="true" href="https://datarist.com/docs/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Docs');">Docs</a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" aria-current="true" href="https://datarist.com/blog/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Blog');">Blog</a>
                  </li>
                </ul>
                <hr className="d-lg-none text-white-50">
                <ul className="navbar-nav flex-row flex-wrap ms-md-auto">
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" href="https://github.com/mydatarist" target="_blank" rel="noopener">
                      <svg className="bi navbar-nav-svg"><use xlink:href="#github"/></svg>
                      <title>Github</title>
                      <small className="d-lg-none ms-2">Github</small>
                    </a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" href="https://twitter.com/datarist" target="_blank" rel="noopener">
                      <svg className="bi navbar-nav-svg"><use xlink:href="#twitter"/></svg>
                      <title>Twitter</title>
                      <small className="d-lg-none ms-2">Twitter</small>
                    </a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" href="https://medium.com/@datarist" target="_blank" rel="noopener">
                      <svg className="bi navbar-nav-svg"><use xlink:href="#medium"/></svg>
                      <title>Medium</title>
                      <small className="d-lg-none ms-2">Medium</small>
                    </a>
                  </li>
                  <li className="nav-item col-6 col-lg-auto">
                    <a className="nav-link py-2 px-0 px-lg-2" href="https://youtube.com/@datarist" target="_blank" rel="noopener">
                      <svg className="bi navbar-nav-svg"><use xlink:href="#youtube"/></svg>
                        <title>YouTube</title>
                        <small className="d-lg-none ms-2">YouTube</small>
                    </a>
                  </li>                         
                  <li className="nav-item py-2 py-lg-1 col-12 col-lg-auto">
                    <div className="vr d-none d-lg-flex h-100 mx-lg-2 text-white"></div>
                    <hr className="d-lg-none my-2 text-white-50">
                  </li>
                  <li className="nav-item dropdown">
                    <button className="btn btn-link nav-link py-2 px-0 px-lg-2 dropdown-toggle d-flex align-items-center"
                      id="dd-theme"
                      type="button"
                      aria-expanded="false"
                      data-bs-toggle="dropdown"
                      data-bs-display="static"
                      aria-label="Toggle theme (auto)">
                      <svg className="bi my-1 theme-icon-active"><use href="#circle-half"></use></svg>
                      <span className="d-lg-none ms-2" id="dd-theme-text">Toggle theme</span>
                    </button>
                    <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="dd-theme-text">
                      <li>
                        <button type="button" className="dropdown-item d-flex align-items-center" data-bs-theme-value="light" aria-pressed="false">
                          <svg className="bi me-2 opacity-50 theme-icon"><use href="#sun-fill"></use></svg>
                          Light
                          <svg className="bi ms-auto d-none"><use href="#check2"></use></svg>
                        </button>
                      </li>
                      <li>
                        <button type="button" className="dropdown-item d-flex align-items-center" data-bs-theme-value="dark" aria-pressed="false">
                          <svg className="bi me-2 opacity-50 theme-icon"><use href="#moon-stars-fill"></use></svg>
                          Dark
                          <svg className="bi ms-auto d-none"><use href="#check2"></use></svg>
                        </button>
                      </li>
                      <li>
                        <button type="button" className="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto" aria-pressed="true">
                          <svg className="bi me-2 opacity-50 theme-icon"><use href="#circle-half"></use></svg>
                          Auto
                          <svg className="bi ms-auto d-none"><use href="#check2"></use></svg>
                        </button>
                      </li>
                    </ul>
                  </li>
                </ul>
              </div>
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