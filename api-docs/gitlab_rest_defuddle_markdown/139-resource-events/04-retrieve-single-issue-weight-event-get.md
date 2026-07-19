# 04-Retrieve single issue weight event [GET]

`GET /api/v4/projects/{id}/issues/{eventable_id}/resource_weight_events/{event_id}`

Retrieves a single weight event for a specified project issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `event_id` | `string` | `path` | Yes | The ID of a resource weight event |
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
  "issue_id": integer,
  "weight": integer,
}
```

#### 400 - Bad Request

#### 404 - Not found

