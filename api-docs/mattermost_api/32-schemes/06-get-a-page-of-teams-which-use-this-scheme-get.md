# 06-Get a page of teams which use this scheme. [GET]

`GET /api/v4/schemes/{scheme_id}/teams`

Get a page of teams which use this scheme. The provided Scheme ID should be for a Team-scoped Scheme.
Use the query parameters to modify the behaviour of this endpoint.

##### Permissions
`manage_system` permission is required.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scheme_id` | `string` | `path` | Yes | Scheme GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of teams per page. |

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

#### 403 - 

#### 404 - 

