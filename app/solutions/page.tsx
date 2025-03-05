import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Solutions",
  description: "Platform solutions to solve your data challenges.",
  alternates: {
    canonical: "https://datarist.com/solutions/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Platform solutions to solve your data challenges.</h1>
    </main>
  );
}