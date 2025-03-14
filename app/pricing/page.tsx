import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Pricing",
  description: "Get the complete data platform.",
  alternates: {
    canonical: "https://datarist.com/pricing/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Get the complete data platform.</h1>
    </main>
  );
}