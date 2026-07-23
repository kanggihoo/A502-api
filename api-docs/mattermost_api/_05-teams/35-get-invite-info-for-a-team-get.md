# 35-Get invite info for a team [GET]

`GET /api/v4/teams/invite/{invite_id}`

Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

__Minimum server version__: 4.0

##### Permissions
No authentication required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `invite_id` | `string` | `path` | Yes | Invite id for a team |

### Responses

#### 200 - Team invite info retrieval successful

Schema (application/json):
```json
{
  "id": string,
  "name": string,
  "display_name": string,
  "description": string,
}
```

#### 400 - 

