# 01-Get the settings manifest for Settings Sync [GET]

`GET /api/v4/vscode/settings_sync(/{settings_context_hash})/v1/manifest`

Get the settings manifest for Settings Sync

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `settings_context_hash` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "latest": string,
  "session": string,
}
```

#### 401 - 401 Unauthorized

#### 404 - Not Found

