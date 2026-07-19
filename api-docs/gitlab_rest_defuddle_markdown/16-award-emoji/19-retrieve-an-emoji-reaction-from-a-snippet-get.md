# 19-Retrieve an emoji reaction from a snippet [GET]

`GET /api/v4/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}`

Retrieves a specified emoji reaction from a snippet. This endpoint can be accessed without authentication if the snippet is publicly accessible.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of the emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `snippet_id` | `integer` | `path` | Yes | The ID of a project snippet |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "user": {
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
  "created_at": string,
  "updated_at": string,
  "awardable_id": integer,
  "awardable_type": string,
  "url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

