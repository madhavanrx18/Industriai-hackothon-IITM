import React from 'react';
import { AuthForm } from './components/AuthForm';
import { ConnectSupabase } from './components/ConnectSupabase';
import { Toaster } from 'react-hot-toast';
import { useSupabase } from './hooks/useSupabase';

function App() {
  const { isReady } = useSupabase();

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex flex-col items-center justify-center p-4">
      {isReady ? <AuthForm /> : <ConnectSupabase />}
      <Toaster position="top-right" />
    </div>
  );
}

export default App;