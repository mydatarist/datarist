import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Resources",
  description: "All Topics.",
  alternates: {
    canonical: "https://datarist.com/resources/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>All Topics</h1>
    </main>
  );
}