import { SignUp } from '@clerk/nextjs'

export default function SignUpPage() {
  return (
    <main className="min-h-screen flex items-center justify-center p-8 bg-white text-gray-900">
      <SignUp routing="path" path="/sign-up" />
    </main>
  )
}

