# 03-Receive Slack events [POST]

`POST /api/v4/integrations/slack/events`

Receive Slack events

### Request Body (application/json)

```json
{
  "token": string, // (Deprecated by Slack) The request token, unused by GitLab
  "team_id": string, // The Slack workspace ID of where the event occurred
  "api_app_id": string, // The Slack app ID
  "event": {}, // The event object with variable properties
  "type": string, // The kind of event this is, usually `event_callback`
  "event_id": string, // A unique identifier for this specific event
  "event_time": integer, // The epoch timestamp in seconds when this event was dispatched
  "authed_users": [
    string
  ], // (Deprecated by Slack) An array of Slack user IDs
}
```
### Responses

#### 200 - Successfully processed event

#### 204 - Failed to process event

#### 400 - Bad Request

#### 401 - Unauthorized

