# 07-Create a Debian group distribution [POST]

`POST /api/v4/groups/{id}/-/debian_distributions`

Creates a Debian group distribution for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "codename": string (required), // The Debian Codename
  "suite": string, // The Debian Suite
  "origin": string, // The Debian Origin
  "label": string, // The Debian Label
  "description": string, // The Debian Description
  "valid_time_duration_seconds": integer, // The duration before the Release file should be considered expired by the client
  "components": [
    string
  ], // The list of Components
  "architectures": [
    string
  ], // The list of Architectures
}
```
### Responses

#### 201 - Created

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

