# 47-Delete a package protection rule [DEL]

`DELETE /api/v4/projects/{id}/packages/protection/rules/{package_protection_rule_id}`

Deletes a package protection rule from a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_protection_rule_id` | `integer` | `path` | Yes | The ID of the package protection rule |

### Responses

#### 204 - 204 No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

