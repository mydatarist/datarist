import type { FormEvent } from "react";
import { Amplify } from "aws-amplify";
import { signUp } from "aws-amplify/auth";
import outputs from "@/amplify_outputs.json";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sign up",
  description: "Create your free account.",
  alternates: {
    canonical: "https://datarist.com/sign-up/",
    languages: {
      "en-us": "https://datarist.com/en-us/",
    },
  },
}

Amplify.configure(outputs)

interface SignUpFormElements extends HTMLFormControlsCollection {
  email: HTMLInputElement
  password: HTMLInputElement
}

interface SignUpForm extends HTMLFormElement {
  readonly elements: SignUpFormElements
}

export default function Page() {  
  async function handleSubmit(event: FormEvent<SignUpForm>) {
    event.preventDefault()
    const form = event.currentTarget
    // ... validate inputs
    await signUp({
      username: form.elements.email.value,
      password: form.elements.password.value,
    })
  }
  return (
    <main>
      <h1>Create your free account.</h1>
    </main>
  );
}