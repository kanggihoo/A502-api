# 06-Delete Pages domain [DEL]

`DELETE /api/v4/projects/{id}/pages/domains/{domain}`

Deletes a specified Pages domain in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `domain` | `string` | `path` | Yes | The domain |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 404 - Not Found

