# 06-Merge topics [POST]

`POST /api/v4/topics/merge`

Merges a source topic into a target topic. This action deletes the source topic and moves all assigned projects to the target topic. Administrators only.

### Request Body (application/json)

```json
{
  "source_topic_id": integer (required), // ID of source project topic
  "target_topic_id": integer (required), // ID of target project topic
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

