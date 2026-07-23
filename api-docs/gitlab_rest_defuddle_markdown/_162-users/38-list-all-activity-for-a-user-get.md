# 38-List all activity for a user [GET]

`GET /api/v4/user/activities`

Lists all activity for a specified user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `from` | `string` | `query` | No | Date string in the format YEAR-MONTH-DAY |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "username": string,
  "last_activity_on": string,
  "last_activity_at": string,
}
```

#### 400 - Bad Request

