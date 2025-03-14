import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact",
  description: "Let's talk about your project.",
  alternates: {
    canonical: "https://datarist.com/contact/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Contact Datarist</h1>
    </main>
  );
}