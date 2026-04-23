import Link from "next/link";

export default function Navbar() {
  return (
    <header className="h-16 bg-white border-b px-6 flex items-center justify-between">
      
      {/* Left: Brand + Nav */}
      <div className="flex items-center gap-8">
        <div>
          <Link href="/" className="text-lg font-bold text-green-500">
            Purity UI
          </Link>
          <p className="text-xs text-gray-400">Admin Dashboard</p>
        </div>

        {/* Nav Links */}
        <nav className="hidden md:flex items-center gap-6 text-sm text-gray-600">
          <Link href="/about" className="hover:text-green-500">
            About
          </Link>
          
        </nav>
      </div>

      {/* Right: Actions */}
      <div className="flex items-center gap-4">
        <input
          placeholder="Search..."
          className="hidden md:block px-3 py-2 text-sm border rounded-lg focus:outline-none"
        />
        <Link href="/signin" className="hover:text-green-500">
          Sign In
        </Link>

        <Link href="/settings" className="hover:text-green-500">
          Settings
        </Link>
        

        <div className="w-9 h-9 rounded-full bg-green-100 flex items-center justify-center text-green-600 font-bold">
          V
        </div>
      </div>

    </header>
  );
}
