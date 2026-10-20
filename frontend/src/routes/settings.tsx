import { createFileRoute } from '@tanstack/react-router';

export const Route = createFileRoute('/settings')({
  component: () => {
    return <div>Hello "/settings"!</div>;
  },
});
