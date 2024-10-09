// contexts/AuthContext.tsx
import { createContext, useState } from 'react';
import { GoogleAuthProvider } from '../providers/GoogleAuthProvider';
import { AuthProvider } from '../interfaces/AuthProvider';

const AuthContext = createContext<AuthProvider | null>(null);

import { ReactNode } from 'react';

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProviderComponent: React.FC<AuthProviderProps> = ({ children }) => {
  const [authProvider] = useState<AuthProvider>(new GoogleAuthProvider()); // Remove setAuthProvider

  return (
    <AuthContext.Provider value={authProvider}> 
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;