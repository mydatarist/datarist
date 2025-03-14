import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Products",
  description: "Platform products to solve your data challenges.",
  alternates: {
    canonical: "https://datarist.com/products/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Platform products to solve your data challenges.</h1>
    </main>
  );
}