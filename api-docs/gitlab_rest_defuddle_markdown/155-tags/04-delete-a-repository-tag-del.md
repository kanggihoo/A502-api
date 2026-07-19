# 04-Delete a repository tag [DEL]

`DELETE /api/v4/projects/{id}/repository/tags/{tag_name}`

Delete a repository tag

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The name of the tag |

### Responses

#### 204 - No Content

#### 400 - Bad request

#### 403 - Unauthenticated

#### 404 - Not found

#### 412 - Precondition failed

