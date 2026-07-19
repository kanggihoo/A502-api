# 12-Delete an approval rule for a project [DEL]

`DELETE /api/v4/projects/{id}/approval_rules/{approval_rule_id}`

Deletes an approval rule for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `approval_rule_id` | `integer` | `path` | Yes | The ID of an approval_rule |

### Responses

#### 204 - No Content

#### 400 - Bad Request

#### 404 - Not Found

