# 06-Create an outgoing webhook [POST]

`POST /api/v4/hooks/outgoing`

Create an outgoing webhook for a team.
##### Permissions
`manage_webhooks` for the team the webhook is in.

`manage_others_outgoing_webhooks` for the team the webhook is in if the user is different than the requester.


### Request Body (application/json)

```json
{
  "team_id": string (required), // The ID of the team that the webhook watchs
  "channel_id": string, // The ID of a public channel that the webhook watchs
  "creator_id": string, // The ID of the owner of the webhook if different than the requester. Required in [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
  "description": string, // The description for this outgoing webhook
  "display_name": string (required), // The display name for this outgoing webhook
  "trigger_words": [
    string
  ] (required), // List of words for the webhook to trigger on
  "trigger_when": integer, // When to trigger the webhook, `0` when a trigger word is present at all and `1` if the message starts with a trigger word
  "callback_urls": [
    string
  ] (required), // The URLs to POST the payloads to when the webhook is triggered
  "content_type": string, // The format to POST the data in, either `application/json` or `application/x-www-form-urlencoded`
}
```
### Responses

#### 201 - Outgoing webhook creation successful

Schema (application/json):
```json
{
  "id": string, // The unique identifier for this outgoing webhook
  "create_at": integer, // The time in milliseconds a outgoing webhook was created
  "update_at": integer, // The time in milliseconds a outgoing webhook was last updated
  "delete_at": integer, // The time in milliseconds a outgoing webhook was deleted
  "creator_id": string, // The Id of the user who created the webhook
  "team_id": string, // The ID of the team that the webhook watchs
  "channel_id": string, // The ID of a public channel that the webhook watchs
  "description": string, // The description for this outgoing webhook
  "display_name": string, // The display name for this outgoing webhook
  "trigger_words": [
    string
  ], // List of words for the webhook to trigger on
  "trigger_when": integer, // When to trigger the webhook, `0` when a trigger word is present at all and `1` if the message starts with a trigger word
  "callback_urls": [
    string
  ], // The URLs to POST the payloads to when the webhook is triggered
  "content_type": string, // The format to POST the data in, either `application/json` or `application/x-www-form-urlencoded`
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

