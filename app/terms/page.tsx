import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Terms",
  description: "Legal.",
  alternates: {
    canonical: "https://datarist.com/terms/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Terms of Use</h1>
    </main>
  );
}