// app/login/page.tsx
'use client';
import { useContext } from 'react';
import AuthContext from '../../contexts/AuthContext';

export default function Login() {
  const authProvider = useContext(AuthContext);
  console.log('AuthProvider:', authProvider); 

  const handleLogin = async () => {
    if (authProvider) {
      await authProvider.login();
    }
  };
return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
        <h1 className="text-4xl font-bold mb-8">Login</h1>
        <button 
            onClick={handleLogin} 
            className="px-6 py-3 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-600 transition duration-300"
        >
            Sign in with Google
        </button>
    </div>
);
}