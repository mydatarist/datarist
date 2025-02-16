import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./app.css";
import Link from "next/link";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Datarist: Data Insights.",
  description: "Empowering people and organizations with data.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
      <header class="navbar navbar-expand-lg bd-navbar sticky-top">
    <nav class="container-xxl bd-gutter flex-wrap flex-lg-nowrap" aria-label="Main navigation">
        <div class="d-lg-none" style="width: 4.25rem;"></div>
        <a class="navbar-brand p-0 me-0 me-lg-2" href="https://datarist.com/" aria-label="Datarist">
          <svg width="24" height="24" class="bi" fill="currentColor"><use href="#logo"></use></svg>
        </a> 
      <div class="d-flex">
        <div class="bd-search" id="docsearch" data-bd-docs-version="5.3"></div>
  
        <button class="navbar-toggler d-flex d-lg-none order-3 p-2" type="button" data-bs-toggle="offcanvas" data-bs-target="#bdNavbar" aria-controls="bdNavbar" aria-label="Toggle navigation">
          <svg class="bi" aria-hidden="true"><use xlink:href="#three-dots"></use></svg>
        </button>
      </div>
  
      <div class="offcanvas-lg offcanvas-end flex-grow-1" tabindex="-1" id="bdNavbar" aria-labelledby="bdNavbarOffcanvasLabel" data-bs-scroll="true">
        <div class="offcanvas-header px-4 pb-0">
          <!--
          <h5 class="offcanvas-title text-white" id="bdNavbarOffcanvasLabel">Datarist</h5> -->
          <a class="navbar-brand" id="bdNavbarOffcanvasLabel" href="https://datarist.com/" aria-label="Datarist">
            <svg width="24" height="24" class="bi" fill="currentColor"><use href="#logo"></use></svg>
          </a>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close" data-bs-target="#bdNavbar"></button>
        </div>
  
        <div class="offcanvas-body p-4 pt-0 p-lg-0">
          <hr class="d-lg-none text-white-50">
          <ul class="navbar-nav flex-row flex-wrap bd-navbar-nav">
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://datarist.com/solutions/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Solutions');">Solutions</a>
            </li>
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://datarist.com/catalog/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Catalog');">Catalog</a>
            </li>
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://datarist.com/docs/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Docs');">Docs</a>
            </li>
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://datarist.com/blog/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Blog');" target="_blank" rel="noopener">Blog</a>
            </li>
          </ul>
  
          <hr class="d-lg-none text-white-50">
  
          <ul class="navbar-nav flex-row flex-wrap ms-md-auto">
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2 btn btn-publish" href="https://datarist.com/publish/" onclick="ga('send', 'event', 'Navbar', 'Community links', 'Publish');">Publish</a>
            </li>
            <li class="nav-item py-2 py-lg-1 col-12 col-lg-auto">
              <div class="vr d-none d-lg-flex h-100 mx-lg-2 text-white"></div>
              <hr class="d-lg-none my-2 text-white-50">
            </li>
  
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://github.com/mydatarist/" target="_blank" rel="noopener">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="navbar-nav-svg" viewBox="0 0 512 499.36" role="img"><title>GitHub</title><path fill="currentColor" fill-rule="evenodd" d="M256 0C114.64 0 0 114.61 0 256c0 113.09 73.34 209 175.08 242.9 12.8 2.35 17.47-5.56 17.47-12.34 0-6.08-.22-22.18-.35-43.54-71.2 15.49-86.2-34.34-86.2-34.34-11.64-29.57-28.42-37.45-28.42-37.45-23.27-15.84 1.73-15.55 1.73-15.55 25.69 1.81 39.21 26.38 39.21 26.38 22.84 39.12 59.92 27.82 74.5 21.27 2.33-16.54 8.94-27.82 16.25-34.22-56.84-6.43-116.6-28.43-116.6-126.49 0-27.95 10-50.8 26.35-68.69-2.63-6.48-11.42-32.5 2.51-67.75 0 0 21.49-6.88 70.4 26.24a242.65 242.65 0 0 1 128.18 0c48.87-33.13 70.33-26.24 70.33-26.24 14 35.25 5.18 61.27 2.55 67.75 16.41 17.9 26.31 40.75 26.31 68.69 0 98.35-59.85 120-116.88 126.32 9.19 7.9 17.38 23.53 17.38 47.41 0 34.22-.31 61.83-.31 70.23 0 6.85 4.61 14.81 17.6 12.31C438.72 464.97 512 369.08 512 256.02 512 114.62 397.37 0 256 0z"/></svg>
                <small class="d-lg-none ms-2">GitHub</small>
              </a>
            </li>
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://twitter.com/datarist/" target="_blank" rel="noopener">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="navbar-nav-svg" viewBox="0 0 512 416.32" role="img"><title>Twitter</title><path fill="currentColor" d="M160.83 416.32c193.2 0 298.92-160.22 298.92-298.92 0-4.51 0-9-.2-13.52A214 214 0 0 0 512 49.38a212.93 212.93 0 0 1-60.44 16.6 105.7 105.7 0 0 0 46.3-58.19 209 209 0 0 1-66.79 25.37 105.09 105.09 0 0 0-181.73 71.91 116.12 116.12 0 0 0 2.66 24c-87.28-4.3-164.73-46.3-216.56-109.82A105.48 105.48 0 0 0 68 159.6a106.27 106.27 0 0 1-47.53-13.11v1.43a105.28 105.28 0 0 0 84.21 103.06 105.67 105.67 0 0 1-47.33 1.84 105.06 105.06 0 0 0 98.14 72.94A210.72 210.72 0 0 1 25 370.84a202.17 202.17 0 0 1-25-1.43 298.85 298.85 0 0 0 160.83 46.92"/></svg>
                <small class="d-lg-none ms-2">Twitter</small>
              </a>
            </li>
            <li class="nav-item col-6 col-lg-auto">
              <a class="nav-link py-2 px-0 px-lg-2" href="https://medium.com/@datarist/" target="_blank" rel="noopener">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="bi navbar-nav-svg"><use xlink:href="#medium"/></svg>
                <title>Medium</title>
                <small class="d-lg-none ms-2">Medium</small>
              </a>
            </li>         
  
  
  
  
            <li class="nav-item py-2 py-lg-1 col-12 col-lg-auto">
              <div class="vr d-none d-lg-flex h-100 mx-lg-2 text-white"></div>
              <hr class="d-lg-none my-2 text-white-50">
            </li>
  
            <li class="nav-item dropdown">
              <button class="btn btn-link nav-link py-2 px-0 px-lg-2 dropdown-toggle d-flex align-items-center"
                    id="bd-theme"
                    type="button"
                    aria-expanded="false"
                    data-bs-toggle="dropdown"
                    data-bs-display="static"
                    aria-label="Toggle theme (auto)">
              <svg class="bi my-1 theme-icon-active"><use href="#circle-half"></use></svg>
              <span class="d-lg-none ms-2" id="bd-theme-text">Toggle theme</span>
            </button>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="bd-theme-text">
                <li>
                  <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="light" aria-pressed="false">
                    <svg class="bi me-2 opacity-50"><use href="#sun-fill"></use></svg>
                    Light
                    <svg class="bi ms-auto d-none"><use href="#check2"></use></svg>
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item d-flex align-items-center" data-bs-theme-value="dark" aria-pressed="false">
                    <svg class="bi me-2 opacity-50"><use href="#moon-stars-fill"></use></svg>
                    Dark
                    <svg class="bi ms-auto d-none"><use href="#check2"></use></svg>
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item d-flex align-items-center active" data-bs-theme-value="auto" aria-pressed="true">
                    <svg class="bi me-2 opacity-50"><use href="#circle-half"></use></svg>
                    Auto
                    <svg class="bi ms-auto d-none"><use href="#check2"></use></svg>
                  </button>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
        
        {children}
        <Link href="/about/">About</Link>
        <Link href="/solutions/">Solutions</Link>
        <Link href="/pricing/">Pricing</Link>
        <Link href="/terms/">Terms</Link>
        <Link href="/privacy/">Privacy</Link>
        <Link href="/cookies/">Cookies</Link>
        <Link href="/contact/">Contact</Link>      
      </body>
    </html>
  );
}
