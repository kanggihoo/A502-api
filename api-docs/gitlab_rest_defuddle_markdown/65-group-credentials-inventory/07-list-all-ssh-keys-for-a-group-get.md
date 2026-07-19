# 07-List all SSH keys for a group [GET]

`GET /api/v4/groups/{id}/manage/ssh_keys`

Lists all SSH public keys associated with enterprise users in a top-level-group. This feature was introduced in GitLab 17.9.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `created_before` | `string` | `query` | No | Filter ssh keys which were created before given datetime |
| `created_after` | `string` | `query` | No | Filter ssh keys which were created after given datetime |
| `expires_before` | `string` | `query` | No | Filter ssh keys which expire before given datetime |
| `expires_after` | `string` | `query` | No | Filter ssh keys which expire after given datetime |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "created_at": string,
  "expires_at": string,
  "last_used_at": string,
  "usage_type": string,
  "user_id": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

