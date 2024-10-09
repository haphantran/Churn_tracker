import { User as SupabaseUser } from '@supabase/supabase-js';



export interface AuthProvider {

  login(): Promise<void>;

  logout(): Promise<void>;

  getUser(): Promise<SupabaseUser | null>;

}