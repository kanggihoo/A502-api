# 02-Create a project topic [POST]

`POST /api/v4/topics`

Creates a project topic. Administrators only.

### Request Body (multipart/form-data)

```json
{
  "name": string (required), // Slug (name)
  "title": string (required), // Title
  "description": string, // Description
  "avatar": string, // Avatar image for topic
  "organization_id": integer, // The organization id for the topic
}
```
### Responses

#### 201 - Created

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

