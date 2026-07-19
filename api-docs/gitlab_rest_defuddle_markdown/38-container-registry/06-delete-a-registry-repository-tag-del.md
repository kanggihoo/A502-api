# 06-Delete a registry repository tag [DEL]

`DELETE /api/v4/projects/{id}/registry/repositories/{repository_id}/tags/{tag_name}`

Deletes a specified container registry repository tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `repository_id` | `integer` | `path` | Yes | The ID of the repository |
| `tag_name` | `string` | `path` | Yes | The name of the tag |

### Responses

#### 204 - Success

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

