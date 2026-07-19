# 05-Create a client key [POST]

`POST /api/v4/projects/{id}/error_tracking/client_keys`

Creates a client key for integrated error tracking in a specified project. The public key attribute is generated automatically.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Responses

#### 201 - Created

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

