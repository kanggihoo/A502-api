# 03-Get a list of references to one or more vscode setting resources [GET]

`GET /api/v4/vscode/settings_sync(/{settings_context_hash})/v1/resource/{resource_name}`

Get a list of references to one or more vscode setting resources

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `resource_name` | `string` | `path` | Yes | Name of the resource such as settings |
| `settings_context_hash` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "url": string,
  "created": string,
}
```

#### 400 - 400 bad request

#### 401 - 401 Unauthorized

#### 404 - Not Found

