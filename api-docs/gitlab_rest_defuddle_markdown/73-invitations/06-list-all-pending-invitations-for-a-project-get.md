# 06-List all pending invitations for a project [GET]

`GET /api/v4/projects/{id}/invitations`

Lists all pending invitations for a specified project viewable by the authenticated user. Returns invitations to direct members only, and not through inherited ancestor groups. This function takes pagination parameters `page` and `per_page` to restrict the list of members.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The project ID |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `query` | `string` | `query` | No | A query string to search for members |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "access_level": string,
  "created_at": string,
  "expires_at": string,
  "invite_email": string,
  "invite_token": string,
  "user_name": string,
  "created_by_name": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

