# 04-Update a project topic [PUT]

`PUT /api/v4/topics/{id}`

Updates a specified project topic. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of project topic |

### Request Body (multipart/form-data)

```json
{
  "name": string, // Slug (name)
  "title": string, // Title
  "description": string, // Description
  "avatar": string, // Avatar image for topic
}
```
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

