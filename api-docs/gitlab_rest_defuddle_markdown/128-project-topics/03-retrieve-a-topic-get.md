# 03-Retrieve a topic [GET]

`GET /api/v4/topics/{id}`

Retrieves a specified project topic.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of project topic |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "title": string,
  "description": string,
  "total_projects_count": integer,
  "organization_id": integer,
  "avatar_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

