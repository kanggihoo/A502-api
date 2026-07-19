# 18-Get the user agent details for a project snippet [GET]

`GET /api/v4/projects/{id}/snippets/{snippet_id}/user_agent_detail`

Get the user agent details for a project snippet

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `snippet_id` | `integer` | `path` | Yes | The ID of a project snippet |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "user_agent": string,
  "ip_address": string,
  "akismet_submitted": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not found

