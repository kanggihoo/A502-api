# 10-Get the teams for a granular data retention policy [GET]

`GET /api/v4/data_retention/policies/{policy_id}/teams`

Gets the teams to which a granular data retention policy is applied.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of teams per page. |

### Responses

#### 200 - Teams for retention policy successfully retrieved.

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

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

