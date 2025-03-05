import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sitemap",
  description: "Sitemap.",
  alternates: {
    canonical: "https://datarist.com/sitemap/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Sitemap.</h1>
    </main>
  );
}