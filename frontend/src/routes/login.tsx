import { createFileRoute } from '@tanstack/react-router';
import { useState } from 'react';
// import axios from "axios";

export const Route = createFileRoute('/login')({
  component: () => {
    const [email, setEmail] = useState('');
    const [sent, _setSent] = useState(false);
    const [loading, setLoading] = useState(false);

    async function handleSubmit(e: React.FormEvent) {
      e.preventDefault();
      setLoading(true);

      // axios.post("http.");
    }
    return (
      <div>
        <form>
          <label>
            Enter your email address to login:
            <input
              type="text"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              // placeholder='hello@tramily.com'
            />
          </label>
        </form>
        <button onClick={handleSubmit} disabled={loading}>
          {loading ? 'Sending...' : 'Log In'}
        </button>
        {sent && <p>Email sent! Please check your email.</p>}
      </div>
    );
  },
});
