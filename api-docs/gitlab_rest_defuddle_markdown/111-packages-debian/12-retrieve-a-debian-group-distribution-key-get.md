# 12-Retrieve a Debian group distribution key [GET]

`GET /api/v4/groups/{id}/-/debian_distributions/{codename}/key.asc`

Retrieves a specified Debian group distribution key for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `codename` | `string` | `path` | Yes | The Debian Codename |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "codename": string,
  "suite": string,
  "origin": string,
  "label": string,
  "version": string,
  "description": string,
  "valid_time_duration_seconds": integer,
  "components": [
    string
  ],
  "architectures": [
    string
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

