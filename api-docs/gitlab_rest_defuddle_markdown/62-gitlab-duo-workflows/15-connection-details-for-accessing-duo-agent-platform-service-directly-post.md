# 15-Connection details for accessing Duo Agent Platform Service directly [POST]

`POST /api/v4/ai/duo_workflows/direct_access`

Connection details for accessing Duo Agent Platform Service directly

### Request Body (application/json)

```json
{
  "workflow_definition": string, // workflow type based on its capability
  "root_namespace_id": string, // the ID of the root namespace
  "project_id": string, // The ID or path of the project
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 429 - Too many requests

