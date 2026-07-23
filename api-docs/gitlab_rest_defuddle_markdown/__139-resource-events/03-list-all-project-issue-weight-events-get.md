# 03-List all project issue weight events [GET]

`GET /api/v4/projects/{id}/issues/{eventable_id}/resource_weight_events`

Lists all weight events for a specified issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `eventable_id` | `any` | `path` | Yes | The ID of the eventable |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

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

#### 404 - Not Found

