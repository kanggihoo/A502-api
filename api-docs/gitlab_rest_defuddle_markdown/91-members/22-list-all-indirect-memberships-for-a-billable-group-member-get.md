# 22-List all indirect memberships for a billable group member [GET]

`GET /api/v4/groups/{id}/billable_members/{user_id}/indirect`

Lists all indirect memberships for a billable member of a group. This operation works on top-level groups only. It does not work on subgroups.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `user_id` | `integer` | `path` | Yes | The user ID of the member |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "source_id": string,
  "source_full_name": string,
  "source_members_url": string,
  "created_at": string,
  "expires_at": string,
  "access_level": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

