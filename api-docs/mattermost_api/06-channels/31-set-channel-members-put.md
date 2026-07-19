# 31-Set channel members [PUT]

`PUT /api/v4/channels/{channel_id}/members`

Set the complete membership list for a channel, with optional channel admin designation.
The server compares the provided list against the current membership and adds or removes
users as needed. Users already in the channel are left untouched (no-op).

When `channel_admins` is provided, a role reconciliation phase runs after membership
changes: listed users are promoted to channel admin, all other members are demoted.
When `channel_admins` is omitted (null), existing admin roles are preserved.

Results are streamed back as NDJSON (`application/x-ndjson`), one line per batch. Each line
is a JSON object with `added`, `removed`, `promoted`, `demoted`, and `errors` arrays for
that batch.

Removals are processed before additions, then role changes. Private channels cannot be
emptied entirely. DM/GM and group-constrained channels are rejected.

#### Example: membership only

Request (using `batch_size=2` and `batch_delay_ms=200`):

```bash
curl -X PUT \
  'https://mattermost.example.com/api/v4/channels/channel123/members?batch_size=2&batch_delay_ms=200' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"members": ["user_id_1", "user_id_2", "user_id_3", "user_id_4"]}'
```

Streamed NDJSON response (one JSON object per line, one line per batch):

```text
{"added":[],"removed":["user_id_5","user_id_6"],"errors":[]}
{"added":["user_id_3","user_id_4"],"removed":[],"errors":[]}
{"added":[],"removed":[],"errors":[{"user_id":"user_id_7","id":"api.channel.add_members.user_denied","error":"user is not a member of the team"}]}
```

In this example, `user_id_1` and `user_id_2` were already members (no-op), `user_id_5` and
`user_id_6` were removed, `user_id_3` and `user_id_4` were added, and `user_id_7` could not
be added because the user is not on the team.

#### Example: membership with admin roles

```bash
curl -X PUT \
  'https://mattermost.example.com/api/v4/channels/channel123/members' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"members": ["user_id_1", "user_id_2", "user_id_3"], "channel_admins": ["user_id_1"]}'
```

Response:

```text
{"added":["user_id_3"],"removed":["user_id_4"]}
{"promoted":["user_id_1"],"demoted":["user_id_2"]}
```

In this example, `user_id_1` was promoted to channel admin and `user_id_2` was demoted.
When `channel_admins` is omitted, existing admin roles are preserved.

__Minimum server version__: 11.7
##### Permissions
Must have `manage_system` permission (system admin only).


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `batch_size` | `integer` | `query` | No | Number of add/remove operations per batch. |
| `batch_delay_ms` | `integer` | `query` | No | Milliseconds to pause between batches, giving the server time to process websocket events and plugin hooks. |

### Request Body (application/json)

```json
{
  "members": [
    string
  ] (required), // User IDs for the desired channel membership. The final membership is the union of `members` and `channel_admins`.
  "channel_admins": [
    string
  ], // User IDs that should have the channel admin role. Users listed here are automatically included in the desired membership (they do not need to also appear in `members`). When null or omitted, existing admin roles are preserved for members who remain in the channel. When present (including empty array), admin roles are set declaratively.
}
```
### Responses

#### 200 - Streamed NDJSON response. Each line is a JSON object representing one batch of results.

If the operation is interrupted (e.g. context cancellation), a final NDJSON line
with an `error` field is emitted so the client can distinguish partial from full
success: `{"error":"The set channel members operation was cancelled."}`


Schema (application/x-ndjson):
```json
any
```

#### 400 - 

#### 401 - 

#### 403 - 

