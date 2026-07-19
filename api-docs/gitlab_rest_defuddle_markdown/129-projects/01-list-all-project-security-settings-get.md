# 01-List all project security settings [GET]

`GET /api/v4/projects/{id}/security_settings`

Lists all security settings for the project. You must have the Security Manager, Developer, Maintainer, or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

