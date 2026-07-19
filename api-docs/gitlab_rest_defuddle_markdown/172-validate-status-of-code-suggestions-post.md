# 172-Validate status of Code Suggestions [POST]

`POST /api/v4/code_suggestions/enabled`

Validates the status Code Suggestions for a specified project. This checks if the project has `code_suggestions` enabled or if an ancestor group has the Code Suggestions add-on enabled.

### Request Body (application/json)

```json
{
  "project_path": string (required), // The path of the project
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - 403 Code Suggestions Disabled

#### 404 - Not found

