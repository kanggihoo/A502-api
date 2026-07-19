# 08-Unpublish Pages [DEL]

`DELETE /api/v4/projects/{id}/pages`

Unpublishes Pages from a specified project. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

