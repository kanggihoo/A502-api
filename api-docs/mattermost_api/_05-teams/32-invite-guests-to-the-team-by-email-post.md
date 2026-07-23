# 32-Invite guests to the team by email [POST]

`POST /api/v4/teams/{team_id}/invite-guests/email`

Invite guests to existing team channels usign the user's email.

The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If the rate limit exceeds, the error message contains details on when to retry and when the timer will be reset.

__Minimum server version__: 5.16

##### Permissions
Must have `invite_guest` permission for the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `graceful` | `boolean` | `query` | No | If true, returns an array with both successful invites and errors instead of aborting on first error. |
| `guest_magic_link` | `boolean` | `query` | No | If true, invites guests with magic link (passwordless) authentication. Requires guest magic link feature to be enabled. |

### Request Body (application/json)

```json
{
  "emails": [
    string
  ] (required), // List of emails
  "channels": [
    string
  ] (required), // List of channel ids
  "message": string, // Message to include in the invite
}
```
### Responses

#### 200 - Guests invite successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

