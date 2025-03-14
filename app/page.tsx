import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Datarist: Data Insights",
  description: "Empowering people and organizations with data.",
  alternates: {
    canonical: "https://www.datarist.com/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    }
  }  
}

export default function App() {  
  return (
    <main>
      <h1>Data Insights</h1>
    </main>
  );
}