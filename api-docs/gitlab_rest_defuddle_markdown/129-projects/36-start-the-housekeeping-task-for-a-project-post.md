# 36-Start the housekeeping task for a project [POST]

`POST /api/v4/projects/{id}/housekeeping`

Starts the housekeeping task for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "task": enum(":eager" | ":prune"), // `prune` to trigger manual prune of unreachable objects or `eager` to trigger eager housekeeping.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Unauthenticated

#### 404 - Not Found

#### 409 - Conflict

