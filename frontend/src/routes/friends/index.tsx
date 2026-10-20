import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/friends/')({
  component: () => {
    return <div>Hello "/friends/"!</div>;
  },
});
