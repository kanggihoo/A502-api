# 02-Get a single issue resource iteration event [GET]

`GET /api/v4/projects/{id}/issues/{eventable_id}/resource_iteration_events/{event_id}`

This feature was introduced in GitLab 13.4

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path the project |
| `event_id` | `string` | `path` | Yes | The ID of a resource iteration event |
| `eventable_id` | `any` | `path` | Yes | The ID of the eventable |

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
  "iteration": {
    "id": integer,
    "iid": integer,
    "sequence": integer,
    "group_id": integer,
    "title": string,
    "description": string,
    "state": integer,
    "created_at": string,
    "updated_at": string,
    "start_date": string,
    "due_date": string,
    "web_url": string,
  },
  "action": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

