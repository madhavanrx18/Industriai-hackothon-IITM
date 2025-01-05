import { useEffect, useState } from 'react';
import { supabaseConfig } from '../config/supabase';
import { supabase } from '../lib/supabase';

export function useSupabase() {
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    setIsReady(supabaseConfig.isConfigured() && supabase !== null);
  }, []);

  return {
    isReady,
    supabase,
  };
}