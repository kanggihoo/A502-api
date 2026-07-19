# 04-Creates or updates a specific setting [POST]

`POST /api/v4/vscode/settings_sync(/{settings_context_hash})/v1/resource/{resource_name}`

Creates or updates a specific setting

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `resource_name` | `string` | `path` | Yes | Name of the resource such as settings |
| `settings_context_hash` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

#### 400 - Bad request

#### 401 - 401 Unauthorized

#### 404 - Not Found

