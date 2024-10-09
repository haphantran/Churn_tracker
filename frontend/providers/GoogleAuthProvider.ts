// providers/GoogleAuthProvider.ts
import { AuthProvider } from '../interfaces/AuthProvider';
import { supabase } from '../utils/supabaseClient';
import { API_BASE_URL } from '../utils/constants';
import { User as SupabaseUser } from '@supabase/supabase-js';

export class GoogleAuthProvider implements AuthProvider {
  async login() {
    const { error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: {
        redirectTo: `http://${API_BASE_URL}/login`,
      }
    });
    if (error) {
      console.error('Error signing in with Google:', error);
      alert('Failed to sign in with Google. Please try again.');
    }
  }

  async logout() {
    await supabase.auth.signOut();
  }

  async getUser(): Promise<SupabaseUser | null> { // Use SupabaseUser type
    const { data: { user } } = await supabase.auth.getUser();
    return user;
  }
}