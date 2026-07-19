# 05-Patch a scheme [PUT]

`PUT /api/v4/schemes/{scheme_id}/patch`

Partially update a scheme by providing only the fields you want to update. Omitted fields will not be updated. The fields that can be updated are defined in the request body, all other provided fields will be ignored.

##### Permissions
`manage_system` permission is required.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scheme_id` | `string` | `path` | Yes | Scheme GUID |

### Request Body (application/json)

```json
{
  "name": string, // The human readable name of the scheme
  "description": string, // The description of the scheme
}
```
### Responses

#### 200 - Scheme patch successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

