# 01-Create a board channel [POST]

`POST /api/v4/boards`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Create a new board channel. Boards are channels with a kanban view backed
by linked properties (status and assignee by default), and live alongside
regular channels but cannot be created or modified through the
`/api/v4/channels` endpoints.

The request body is a `Channel` object whose `type` must be `BO`
(open board) or `BP` (private board). `team_id` and `display_name` are
required.

This endpoint is gated behind the `IntegratedBoards` feature flag. When
the flag is off, the route is not registered and requests return `404`.

##### Permissions
Must have `create_public_channel` for type `BO`, or
`create_private_channel` for type `BP`, on the target team.


### Request Body (application/json)

```json
{
  "team_id": string (required), // The team ID the board belongs to
  "type": enum("BO" | "BP") (required), // The board channel type. * `BO` - open board (visible to all team members) * `BP` - private board (visible to invited members) 
  "display_name": string (required), // Human-readable name shown in the UI. Must not be empty.
  "name": string, // URL-safe channel name. Auto-generated if omitted.
  "header": string,
  "purpose": string,
}
```
### Responses

#### 201 - Board channel creation successful

Schema (application/json):
```json
{
  "id": string,
  "create_at": integer, // The time in milliseconds a channel was created
  "update_at": integer, // The time in milliseconds a channel was last updated
  "delete_at": integer, // The time in milliseconds a channel was deleted
  "team_id": string,
  "type": string,
  "display_name": string,
  "name": string,
  "header": string,
  "purpose": string,
  "last_post_at": integer, // The time in milliseconds of the last post of a channel
  "total_msg_count": integer,
  "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
  "creator_id": string,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

