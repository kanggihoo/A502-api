# 32-Import members [POST]

`POST /api/v4/projects/{id}/import_project_members/{project_id}`

Imports members from another project. If the role of the importing member for the target project is a Maintainer, then members with the Owner role for the source project are imported with the Maintainer role. If the importing member is an Owner, then members with the Owner role for the source project are imported with the Owner role.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `project_id` | `integer` | `path` | Yes | The ID of the source project to import the members from. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 403 - Forbidden - Project

#### 404 - Project Not Found

#### 422 - Import failed

