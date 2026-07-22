# 31-Retrieve an emoji reaction from an epic comment [GET]

`GET /api/v4/groups/{id}/epics/{epic_iid}/notes/{note_id}/award_emoji/{award_id}`

Retrieves a specified emoji reaction from a comment on an epic. This endpoint can be accessed without authentication if the comment is publicly accessible.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of the emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of a group epic |
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

