import React from 'react';
import { AlertCircle } from 'lucide-react';

export function ConnectSupabase() {
  return (
    <div className="bg-yellow-50 border-l-4 border-yellow-400 p-4 max-w-md mx-auto rounded-md">
      <div className="flex items-center">
        <div className="flex-shrink-0">
          <AlertCircle className="h-5 w-5 text-yellow-400" />
        </div>
        <div className="ml-3">
          <h3 className="text-sm font-medium text-yellow-800">
            Supabase Connection Required
          </h3>
          <div className="mt-2 text-sm text-yellow-700">
            <p>
              Please click the "Connect to Supabase" button in the top right corner
              to set up your database connection.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}