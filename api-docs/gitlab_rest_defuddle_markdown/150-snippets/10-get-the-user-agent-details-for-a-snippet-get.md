# 10-Get the user agent details for a snippet [GET]

`GET /api/v4/snippets/{id}/user_agent_detail`

Get the user agent details for a snippet

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a snippet |

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

