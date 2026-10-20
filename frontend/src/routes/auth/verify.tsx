import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/auth/verify')({
  component: () => {
    return <div>Hello "/auth/verify"!</div>;
  },
});
