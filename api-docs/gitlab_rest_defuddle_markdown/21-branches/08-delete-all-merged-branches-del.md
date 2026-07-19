# 08-Delete all merged branches [DEL]

`DELETE /api/v4/projects/{id}/repository/merged_branches`

Deletes all branches that are merged into the default branch for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 202 - 202 Accepted

#### 400 - Bad Request

#### 404 - 404 Project Not Found

