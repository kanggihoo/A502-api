# 01-Get common teams for members of a Group Message. [GET]

`GET /api/v4/channels/{channel_id}/common_teams`

Gets all the common teams for all active members of a Group Message channel.
Returns empty list of no common teams are found.

__Minimum server version__: 9.1

##### Permissions
Must be authenticated and have the `read_channel` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Common teams retrieval successful

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

