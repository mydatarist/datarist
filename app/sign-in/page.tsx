import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sign in",
  description: "Sign in to Datarist",
  alternates: {
    canonical: "https://datarist.com/sign-in/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Sign in to Datarist.</h1>
    </main>
  );
}