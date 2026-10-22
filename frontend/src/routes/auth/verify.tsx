
import { useEffect } from 'react';
import axios from 'axios';
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/auth/verify')({
  component: () => {
  return <div>Verifying your login...</div>
}),
})

useEffect(() => {
  axios.post('/api/auth/verify/', null, {
    params: {
      "token"
    }
  })
  .then((response) => {
    console.log(response.data);
      // Handle data
  })
  .catch((error) => {
    console.log(error);
  })
});