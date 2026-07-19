# 05-Delete feature flag user list [DEL]

`DELETE /api/v4/projects/{id}/feature_flags_user_lists/{iid}`

Deletes a specified feature flag user list.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `iid` | `any` | `path` | Yes | The internal ID of the project's feature flag user list |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

#### 409 - Conflict

