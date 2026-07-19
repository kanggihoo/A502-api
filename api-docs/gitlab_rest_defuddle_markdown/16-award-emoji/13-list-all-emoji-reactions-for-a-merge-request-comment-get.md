# 13-List all emoji reactions for a merge request comment [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/notes/{note_id}/award_emoji`

Lists all emoji reactions for a specified comment on a merge request. This endpoint can be accessed without authentication if the comment is publicly accessible.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |
| `note_id` | `any` | `path` | Yes |  |

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

