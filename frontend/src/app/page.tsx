import Link from 'next/link'
import { SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/nextjs'

export default function Page() {
  return (
    <main className="min-h-screen flex items-center justify-center p-8 bg-white text-gray-900">
      <header className="absolute top-4 right-4">
        <SignedIn>
          <UserButton afterSignOutUrl="/" />
        </SignedIn>
        <SignedOut>
          <SignInButton />
        </SignedOut>
      </header>
      <div className="text-center space-y-4">
        <h1 className="text-3xl font-semibold">NeuroSpace</h1>
        <p className="text-gray-600">Your AI-Powered Second Brain, Reimagined.</p>
        <SignedIn>
          <Link className="inline-block rounded-md bg-gray-900 text-white px-4 py-2" href="/dashboard">Go to Dashboard</Link>
        </SignedIn>
        <SignedOut>
          <p className="text-gray-500">Sign in to access your dashboard.</p>
        </SignedOut>
      </div>
    </main>
  )
}

