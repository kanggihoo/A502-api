# 04-List all project client keys [GET]

`GET /api/v4/projects/{id}/error_tracking/client_keys`

Lists all integrated error tracking client keys for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "active": boolean,
  "public_key": string,
  "sentry_dsn": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

