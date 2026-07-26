# 04-Execute a dialog action button [POST]

`POST /api/v4/actions/dialogs/execute`

Endpoint used by the Mattermost clients when a user clicks an `action_button` element inside an interactive dialog. The server generates a new trigger ID and forwards the button's context to the integration URL; the integration can then open a child (stacked) dialog with that trigger ID. See https://docs.mattermost.com/developer/interactive-dialogs.html for more information on interactive dialogs.

This request is always processed server-side. The client caps the number of simultaneously open interactive dialogs at 3, so if the resulting `open_dialog` event would exceed that limit the client silently skips rendering the additional dialog.

__Minimum server version: 11.10__


### Request Body (application/json)

```json
{
  "url": string (required), // The action button URL to send the action payload to. Must be a valid lookup URL.
  "context": {}, // String map of context values configured on the action button, forwarded to the integration
  "channel_id": string (required), // Channel ID the user clicked the action button from
  "team_id": string, // Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team). 
}
```
### Responses

#### 200 - Dialog action executed successfully

Schema (application/json):
```json
{
  "status": string, // Status of the request ("OK")
  "trigger_id": string, // New trigger ID the integration can use to open a child dialog
}
```

#### 400 - 

#### 401 - 

#### 403 - 

