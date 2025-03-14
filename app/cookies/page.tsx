import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Cookies",
  description: "Websites, Communications and Cookies Privacy Notice.",
  alternates: {
    canonical: "https://datarist.com/cookies/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Cookies</h1>
    </main>
  );
}