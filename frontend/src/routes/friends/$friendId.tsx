import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/friends/$friendId')({
  component: FriendComponent,
})

function FriendComponent() {
  // TanStack Router provides strict type safety for your params
  const { friendId } = Route.useParams()
  return <div>Viewing transit line for Friend: {friendId}</div>
}
