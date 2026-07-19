# 02-Get a specific setting resource [GET]

`GET /api/v4/vscode/settings_sync(/{settings_context_hash})/v1/resource/{resource_name}/{id}`

Get a specific setting resource

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `resource_name` | `string` | `path` | Yes | Name of the resource such as settings |
| `id` | `string` | `path` | Yes | ID of the resource to retrieve |
| `settings_context_hash` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "content": string,
  "machines": string,
  "version": string,
  "machineId": string,
}
```

#### 204 - No content

#### 400 - 400 bad request

#### 401 - 401 Unauthorized

#### 404 - Not Found

