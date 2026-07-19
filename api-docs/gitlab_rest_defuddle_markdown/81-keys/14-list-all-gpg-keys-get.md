# 14-List all GPG keys [GET]

`GET /api/v4/user/gpg_keys`

Lists all GPG keys for the currently authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "key": string,
  "created_at": string,
}
```

#### 400 - Bad Request

