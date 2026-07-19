# 03-Retrieve a feature flag user list [GET]

`GET /api/v4/projects/{id}/feature_flags_user_lists/{iid}`

Retrieves a specified feature flag user list.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `iid` | `any` | `path` | Yes | The internal ID of the project's feature flag user list |

### Responses

#### 200 - OK

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

