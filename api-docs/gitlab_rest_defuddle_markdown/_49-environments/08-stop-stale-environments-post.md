# 08-Stop stale environments [POST]

`POST /api/v4/projects/{id}/environments/stop_stale`

Stops all environments that were last modified or deployed to before a specified date. Excludes protected environments.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "before": string (required), // Stop all environments that were last modified or deployed to before this date.
}
```
### Responses

#### 201 - Created

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

