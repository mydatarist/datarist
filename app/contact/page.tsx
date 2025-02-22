import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Contact",
  description: "Let's talk about your project."
  canonical: "https://www.datarist.com/contact/",
}

export default function Page() {  
  return (
    <main>
      <h1>Contact Datarist</h1>
    </main>
  );
}