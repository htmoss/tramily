import { useEffect } from 'react';
import axios from 'axios';
import { createFileRoute } from '@tanstack/react-router';
import { z } from 'zod';

const searchSchema = z.object({
  token: z.string().catch(''), // Defaults to empty string if missing
});

export const Route = createFileRoute('/auth/verify')({
  validateSearch: searchSchema,
  component: () => {
    // Retrieve the token from the URL search parameters
    const { token } = Route.useSearch();

    useEffect(() => {
      if (!token) return;

      axios
        .post('/api/auth/verify/', null, {
          params: {
            token: token, // Correct key-value pair
          },
        })
        .then((response) => {
          console.log(response.data);
          // Handle successful verification (e.g., redirect or update state)
          console.log('verifying now');
        })
        .catch((error) => {
          console.error('Verification failed:', error);
        });
    }, [token]); // Runs once when the token is available

    return <div>{token ? 'Verifying your login...' : 'No verification token provided.'}</div>;
  },
});
