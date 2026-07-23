# 13-Delete a project deploy token [DEL]

`DELETE /api/v4/projects/{id}/deploy_tokens/{token_id}`

Deletes a project deploy token.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `token_id` | `integer` | `path` | Yes | The ID of the deploy token |

### Responses

#### 204 - Resource deleted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

