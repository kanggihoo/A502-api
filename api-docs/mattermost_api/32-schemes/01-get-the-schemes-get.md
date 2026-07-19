# 01-Get the schemes. [GET]

`GET /api/v4/schemes`

Get a page of schemes. Use the query parameters to modify the behaviour of this endpoint.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scope` | `string` | `query` | No | Limit the results returned to the provided scope, either `team` or `channel`. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of schemes per page. |

### Responses

#### 200 - Scheme list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string, // The unique identifier of the scheme.
    "name": string, // The human readable name for the scheme.
    "description": string, // A human readable description of the scheme.
    "create_at": integer, // The time at which the scheme was created.
    "update_at": integer, // The time at which the scheme was last updated.
    "delete_at": integer, // The time at which the scheme was deleted.
    "scope": string, // The scope to which this scheme can be applied, either "team" or "channel".
    "default_team_admin_role": string, // The id of the default team admin role for this scheme.
    "default_team_user_role": string, // The id of the default team user role for this scheme.
    "default_channel_admin_role": string, // The id of the default channel admin role for this scheme.
    "default_channel_user_role": string, // The id of the default channel user role for this scheme.
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

