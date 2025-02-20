"use client";

import type { Metadata } from "next";
import { generateClient } from "aws-amplify/data";
import type { Schema } from "@/amplify/data/resource";
import { Amplify } from "aws-amplify";
import outputs from "@/amplify_outputs.json";
import "@aws-amplify/ui-react/styles.css";

Amplify.configure(outputs);

const client = generateClient<Schema>();

export const metadata: Metadata = {
  title: {
    absolute: "Datarist",
  },
}

export default function App() {  
  return (
    <main>
      <h1>Data Insights</h1>
    </main>
  );
}