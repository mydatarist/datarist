import type { Metadata, generateMetadata } from "next";
import "./globals.css";
import Link from "next/link";
import Image from "next/image";

export const metadataConfig = {
  "/": {
    title: "Home | Free Background Remove",
    description: "Home page of the best free background remover tool.",
    canonical: "https://www.datarist.com/",
  },
  "/about": {
    title: "About Us | Free Background Remove",
    description:
      "Learn more about the team behind the background remover tool.",
    canonical: "https://www.datarist.com/about",
  },
  "/contact": {
    title: "Contact Us | Free Background Remove",
    description: "Get in touch with us for inquiries or support.",
    canonical: "https://www.datarist.com/contact",
  },
};

export async function generateMetadata({
  params,
}: {
  params: { slug: string };
}): Promise<Metadata> {
  const slug = params.slug || ""; // Ensure slug is always a string
  const pathname = slug ? `/${slug}` : "/"; // Use '/' for home
  const metadata = metadataConfig[pathname as keyof typeof metadataConfig];

  if (!metadata) {
    return {
      title: "Default Title",
      description: "Default description.",
    };
  }

  return {
    title: metadata.title,
    description: metadata.description,
  };
}

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