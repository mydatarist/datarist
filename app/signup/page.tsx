import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sign-up",
  description: "Create your free account",
  alternates: {
    canonical: "https://datarist.com/signup/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

export default function Page() {  
  return (
    <main>
      <h1>Create your free account.</h1>
    </main>
  );
}