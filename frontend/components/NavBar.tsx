// components/NavBar.tsx
import Link from "next/link";

export default function NavBar() {
  return (
    <nav className="bg-gray-800">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Link href="/" legacyBehavior>
                <a className="text-white font-bold text-xl">
                  Credit Card Tracker
                </a>
              </Link>
            </div>
            <div className="hidden md:block">
              <div className="ml-10 flex items-baseline space-x-4">
                <Link href="/credit-cards" legacyBehavior>
                  <a className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">
                    Credit Cards
                  </a>
                </Link>
                <Link href="/login" legacyBehavior>
                  <a className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">
                    Login  
                  </a>
                </Link>
                {/* Add more links for other pages as needed */}
              </div>
            </div>
          </div>
          {/* ... (add login/logout button or user profile section here) */}
        </div>
      </div>
    </nav>
  );
}
