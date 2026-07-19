# 51-Delete a container registry protection tag rule [DEL]

`DELETE /api/v4/projects/{id}/registry/protection/tag/rules/{protection_rule_id}`

Deletes a container registry protection tag rule from a project. This feature was introduced in GitLab 18.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `protection_rule_id` | `integer` | `path` | Yes | The ID of the container protection tag rule. |

### Responses

#### 204 - Delete a container protection tag rule

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

