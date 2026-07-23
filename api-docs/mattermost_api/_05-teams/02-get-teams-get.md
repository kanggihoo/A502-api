# 02-Get teams [GET]

`GET /api/v4/teams`

For regular users only returns open teams. Users with the "manage_system" permission will return teams regardless of type. The result is based on query string parameters - page and per_page.
##### Permissions
Must be authenticated. "manage_system" permission is required to show all teams.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of teams per page. |
| `include_total_count` | `boolean` | `query` | No | Appends a total count of returned teams inside the response object - ex: `{ "teams": [], "total_count" : 0 }`.       |
| `exclude_policy_constrained` | `boolean` | `query` | No | If set to true, teams which are part of a data retention policy will be excluded. The `sysconsole_read_compliance` permission is required to use this parameter.<br>__Minimum server version__: 5.35 |

### Responses

#### 200 - Team list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a team was created
    "update_at": integer, // The time in milliseconds a team was last updated
    "delete_at": integer, // The time in milliseconds a team was deleted
    "display_name": string,
    "name": string,
    "description": string,
    "email": string,
    "type": string,
    "allowed_domains": string,
    "invite_id": string,
    "allow_open_invite": boolean,
    "policy_id": string, // The data retention policy to which this team has been assigned. If no such policy exists, or the caller does not have the `sysconsole_read_compliance_data_retention` permission, this field will be null.
  }
]
```

#### 400 - 

#### 401 - 

