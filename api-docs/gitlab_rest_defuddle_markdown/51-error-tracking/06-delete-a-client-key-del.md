# 06-Delete a client key [DEL]

`DELETE /api/v4/projects/{id}/error_tracking/client_keys/{key_id}`

Deletes an integrated error tracking client key from a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `key_id` | `any` | `path` | Yes |  |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "active": boolean,
  "public_key": string,
  "sentry_dsn": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

