# 01-Create an incoming webhook [POST]

`POST /api/v4/hooks/incoming`

Create an incoming webhook for a channel.
##### Permissions
`manage_webhooks` for the team the webhook is in.

`manage_others_incoming_webhooks` for the team the webhook is in if the user is different than the requester.


### Request Body (application/json)

```json
{
  "channel_id": string (required), // The ID of a public channel or private group that receives the webhook payloads.
  "user_id": string, // The ID of the owner of the webhook if different than the requester. Required for [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
  "display_name": string, // The display name for this incoming webhook
  "description": string, // The description for this incoming webhook
  "username": string, // The username this incoming webhook will post as.
  "icon_url": string, // The profile picture this incoming webhook will use when posting.
  "channel_locked": boolean, // Whether the webhook is locked to the channel.
}
```
### Responses

#### 201 - Incoming webhook creation successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier for this incoming webhook
  "create_at": integer, // The time in milliseconds a incoming webhook was created
  "update_at": integer, // The time in milliseconds a incoming webhook was last updated
  "delete_at": integer, // The time in milliseconds a incoming webhook was deleted
  "last_used": integer, // The time in milliseconds this incoming webhook was last used to post a message
  "channel_id": string, // The ID of a public channel or private group that receives the webhook payloads
  "description": string, // The description for this incoming webhook
  "display_name": string, // The display name for this incoming webhook
}
```

#### 400 - 

#### 401 - 

#### 403 - 

