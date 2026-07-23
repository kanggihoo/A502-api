# 26-Add an emoji reaction to an epic [POST]

`POST /api/v4/groups/{id}/epics/{epic_iid}/award_emoji`

Adds an emoji reaction to an epic.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `epic_iid` | `integer` | `path` | Yes | The internal ID of a group epic |

### Request Body (application/json)

```json
{
  "name": string (required), // Name of the emoji without colons.
}
```
### Responses

#### 201 - Created

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

