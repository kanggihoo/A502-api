# 26-List all project and group memberships for a user [GET]

`GET /api/v4/users/{user_id}/memberships`

Lists all project and group memberships for a specified user. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the user |
| `type` | `string` | `query` | No | Filter memberships by type |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "source_id": string,
  "source_name": string,
  "source_type": string,
  "access_level": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

