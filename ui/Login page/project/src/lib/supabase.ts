import { createClient } from '@supabase/supabase-js';
import { supabaseConfig } from '../config/supabase';
import type { Database } from '../types/supabase';

export const createSupabaseClient = () => {
  if (!supabaseConfig.isConfigured()) {
    return null;
  }
  
  return createClient<Database>(
    supabaseConfig.url,
    supabaseConfig.anonKey
  );
};

export const supabase = createSupabaseClient();