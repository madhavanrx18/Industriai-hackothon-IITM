import { Database } from '../types/supabase';

export const supabaseConfig = {
  url: import.meta.env.VITE_SUPABASE_URL,
  anonKey: import.meta.env.VITE_SUPABASE_ANON_KEY,
  isConfigured(): boolean {
    return Boolean(this.url && this.anonKey);
  }
};