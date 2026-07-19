# 55-Delete a container repository protection rule [DEL]

`DELETE /api/v4/projects/{id}/registry/protection/repository/rules/{protection_rule_id}`

Deletes a specified container repository protection rule.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `protection_rule_id` | `integer` | `path` | Yes | The ID of the container protection rule |

### Responses

#### 204 - 204 No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

