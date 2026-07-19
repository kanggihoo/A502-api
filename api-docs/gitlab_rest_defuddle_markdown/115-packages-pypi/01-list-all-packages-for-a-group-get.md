# 01-List all packages for a group [GET]

`GET /api/v4/groups/{id}/-/packages/pypi/simple`

Lists all packages for a specified group in an HTML file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or full path of the group. |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

