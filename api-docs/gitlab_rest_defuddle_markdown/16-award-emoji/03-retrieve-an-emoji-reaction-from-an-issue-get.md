# 03-Retrieve an emoji reaction from an issue [GET]

`GET /api/v4/projects/{id}/issues/{issue_iid}/award_emoji/{award_id}`

Retrieves a specified emoji reaction from an issue. This endpoint can be accessed without authentication if the issue is publicly accessible.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of the emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of an issuable |

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

