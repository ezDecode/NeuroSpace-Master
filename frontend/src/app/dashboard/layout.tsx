import type { ReactNode } from 'react'
import { UserButton } from '@clerk/nextjs'

export default function DashboardLayout({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-white text-gray-900">
      <nav className="flex items-center justify-between px-6 py-4 border-b border-gray-200">
        <div className="font-medium">NeuroSpace</div>
        <UserButton afterSignOutUrl="/" />
      </nav>
      {children}
    </div>
  )
}

