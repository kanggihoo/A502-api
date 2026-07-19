# 06-Patch a team [PUT]

`PUT /api/v4/teams/{team_id}/patch`

Partially update a team by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored.
##### Permissions
Must have the `manage_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
{
  "display_name": string,
  "description": string,
  "company_name": string,
  "invite_id": string,
  "allow_open_invite": boolean,
}
```
### Responses

#### 200 - team patch successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - 

