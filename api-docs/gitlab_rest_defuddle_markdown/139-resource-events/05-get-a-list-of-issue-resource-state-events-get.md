# 05-Get a list of issue resource state events [GET]

`GET /api/v4/projects/{id}/issues/{eventable_id}/resource_state_events`

Get a list of issue resource state events

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a project |
| `eventable_id` | `integer` | `path` | Yes | The IID of the issue |
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
  "resource_type": string,
  "resource_id": integer,
  "source_commit": string,
  "source_merge_request_id": integer,
  "state": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

