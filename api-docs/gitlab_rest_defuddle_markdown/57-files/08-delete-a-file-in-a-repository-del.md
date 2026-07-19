# 08-Delete a file in a repository [DEL]

`DELETE /api/v4/projects/{id}/repository/files/{file_path}`

Deletes a specified file in a repository. Use the Commits API to delete multiple files with a single request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `file_path` | `string` | `path` | Yes | The URL-encoded path to the file. |
| `branch` | `string` | `query` | Yes | Name of the branch to commit into. To create a new branch, also provide `start_branch`. |
| `commit_message` | `string` | `query` | Yes | Commit message |
| `start_branch` | `string` | `query` | No | Name of the branch to start the new commit from |
| `author_email` | `string` | `query` | No | The email of the author |
| `author_name` | `string` | `query` | No | The name of the author |
| `last_commit_id` | `string` | `query` | No | Last known file commit id |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

