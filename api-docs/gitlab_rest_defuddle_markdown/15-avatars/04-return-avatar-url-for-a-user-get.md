# 04-Return avatar url for a user [GET]

`GET /api/v4/avatar`

Return avatar url for a user

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `email` | `string` | `query` | Yes | Public email address of the user |
| `size` | `integer` | `query` | No | Single pixel dimension for Gravatar images |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "avatar_url": string,
}
```

#### 400 - Bad Request

