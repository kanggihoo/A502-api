# 12-The NuGet V2 Feed Enumerate Packages endpoint [GET]

`GET /api/v4/projects/{project_id}/packages/nuget/v2/Packages\(\)`

This feature was introduced in GitLab 16.4

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `project_id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `$filter` | `string` | `query` | Yes | The NuGet package name |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

