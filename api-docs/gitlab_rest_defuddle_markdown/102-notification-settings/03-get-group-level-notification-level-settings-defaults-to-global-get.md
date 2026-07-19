# 03-Get group level notification level settings, defaults to Global [GET]

`GET /api/v4/groups/{id}/notification_settings`

This feature was introduced in GitLab 8.12

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "level": string,
  "events": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

