# 20-Delete an emoji reaction from a snippet [DEL]

`DELETE /api/v4/projects/{id}/snippets/{snippet_id}/award_emoji/{award_id}`

Deletes a specified emoji reaction from a snippet. Only an administrator or the user who added the reaction can delete it.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `award_id` | `integer` | `path` | Yes | ID of an emoji reaction. |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `snippet_id` | `integer` | `path` | Yes | The ID of a project snippet |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

