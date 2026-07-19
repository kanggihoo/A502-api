# 04-Delete multiple registry repository tags [DEL]

`DELETE /api/v4/projects/{id}/registry/repositories/{repository_id}/tags`

Deletes multiple registry repository tags based on the specified criteria.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `repository_id` | `integer` | `path` | Yes | The ID of the repository |
| `name_regex_delete` | `string` | `query` | No | The tag name regexp to delete, specify .* to delete all |
| `name_regex` | `string` | `query` | No | The tag name regexp to delete, specify .* to delete all |
| `name_regex_keep` | `string` | `query` | No | The tag name regexp to retain |
| `keep_n` | `integer` | `query` | No | Keep n of latest tags with matching name |
| `older_than` | `string` | `query` | No | Delete older than: 1h, 1d, 1month |

### Responses

#### 204 - Success

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

