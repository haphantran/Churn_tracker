// pages/login.tsx
import { useContext } from 'react';
import AuthContext from '../contexts/AuthContext';

export default function Login() {
  const authProvider = useContext(AuthContext);
  console.log('AuthProvider:', authProvider); 
  const handleLogin = async () => {
    if (authProvider) {
      await authProvider.login();
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <button onClick={handleLogin}>Sign in with Google</button>
    </div>
  );
}