# 07-Track an internal GitLab event [POST]

`POST /api/v4/usage_data/track_event`

Tracks a GitLab internal event. This action increments Service Ping counters in Redis and is optionally sent to Snowplow. Introduced in GitLab 16.2.

### Request Body (application/json)

```json
{
  "event": string (required), // The event name that should be tracked
  "namespace_id": integer, // Namespace ID
  "project_id": integer, // Project ID
  "project_path": string, // Project path (used to resolve project_id if not provided)
  "additional_properties": {}, // Additional properties to be tracked
  "send_to_snowplow": boolean, // Send the tracked event to Snowplow
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

