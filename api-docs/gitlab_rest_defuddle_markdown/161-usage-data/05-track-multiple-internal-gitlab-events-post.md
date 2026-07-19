# 05-Track multiple internal GitLab events [POST]

`POST /api/v4/usage_data/track_events`

Tracks one or more GitLab internal events in a single request. Each event increments Service Ping counters in Redis and is optionally sent to Snowplow. This feature was introduced in GitLab 17.3.

### Request Body (application/json)

```json
{
  "events": [
    {}
  ] (required), // An array of internal events. Maximum 50 events allowed.
}
```
### Responses

#### 200 - OK

#### 400 - Validation error

#### 401 - Unauthorized

