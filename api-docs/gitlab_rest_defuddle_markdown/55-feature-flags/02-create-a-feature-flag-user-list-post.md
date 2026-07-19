# 02-Create a feature flag user list [POST]

`POST /api/v4/projects/{id}/feature_flags_user_lists`

Creates a feature flag user list in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the list
  "user_xids": string (required), // A comma separated list of external user ids
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "iid": integer,
  "name": string,
  "user_xids": string,
  "project_id": integer,
  "created_at": string,
  "updated_at": string,
  "path": string,
  "edit_path": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

