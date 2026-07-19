# 03-Create a trigger token [POST]

`POST /api/v4/projects/{id}/triggers`

Creates a pipeline trigger token for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "description": string (required), // The trigger token description
  "expires_at": string, // Timestamp of when the pipeline trigger token expires.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "token": string,
  "description": string,
  "created_at": string,
  "updated_at": string,
  "last_used": string,
  "expires_at": string,
  "owner": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

