# 05-Update a pipeline trigger token [PUT]

`PUT /api/v4/projects/{id}/triggers/{trigger_id}`

Updates a pipeline trigger token for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `trigger_id` | `integer` | `path` | Yes | The trigger token ID |

### Request Body (application/json)

```json
{
  "description": string, // The trigger token description
}
```
### Responses

#### 200 - OK

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

