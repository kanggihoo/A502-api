# 12-Get a single issue resource label event [GET]

`GET /api/v4/projects/{id}/issues/{eventable_id}/resource_label_events/{event_id}`

This feature was introduced in 11.3

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `event_id` | `string` | `path` | Yes | The ID of a resource label event |
| `eventable_id` | `any` | `path` | Yes | The IID of the issue |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
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
  "resource_type": string,
  "resource_id": integer,
  "label": {
    "id": integer,
    "name": string,
    "description": string,
    "text_color": string,
    "description_html": string,
    "color": string,
    "archived": boolean,
  },
  "action": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

