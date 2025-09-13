import Link from 'next/link'
import { currentUser } from '@clerk/nextjs/server'

export default async function DashboardPage() {
  const user = await currentUser()
  return (
    <main className="min-h-screen p-8 bg-white text-gray-900">
      <div className="max-w-2xl mx-auto space-y-4">
        <h1 className="text-2xl font-semibold">Dashboard</h1>
        <p className="text-gray-600">
          Welcome{user?.firstName ? `, ${user.firstName}` : ''}.
        </p>
        <Link className="text-gray-900 underline" href="/">Back to Home</Link>
      </div>
    </main>
  )
}

