# 04-Update a feature flag user list [PUT]

`PUT /api/v4/projects/{id}/feature_flags_user_lists/{iid}`

Updates a specified feature flag user list.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `iid` | `any` | `path` | Yes | The internal ID of the project's feature flag user list |

### Request Body (application/json)

```json
{
  "name": string, // The name of the list
  "user_xids": string, // A comma separated list of external user ids
}
```
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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

