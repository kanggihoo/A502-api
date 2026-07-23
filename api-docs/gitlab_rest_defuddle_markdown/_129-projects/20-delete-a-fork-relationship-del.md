# 20-Delete a fork relationship [DEL]

`DELETE /api/v4/projects/{id}/fork`

Deletes a fork relationship between projects.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 204 - No Content

#### 304 - Not modified

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

