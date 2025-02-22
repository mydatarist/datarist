import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Privacy",
  description: "Our Privacy Notices describe the data our products and services receive, share, and use, as well as choices available to you.",
  alternates: {
    canonical: "https://datarist.com/privacy/",
    languages: {
      "en-US": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Privacy Policy</h1>
    </main>
  );
}