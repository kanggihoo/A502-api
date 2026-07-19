# 171-Retrieve direct connection details for the AI Gateway [POST]

`POST /api/v4/code_suggestions/direct_access`

Retrieves user-specific connection details which can be used by IDEs or clients to send `completion` requests to Code Suggestions directly through the AI Gateway.

### Request Body (application/json)

```json
{
  "project_path": string, // The path of the project
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 429 - Too many requests

