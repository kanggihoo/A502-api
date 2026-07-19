# 07-Check if user can DM another user in shared channels context [GET]

`GET /api/v4/sharedchannels/users/{user_id}/can_dm/{other_user_id}`

Checks if a user can send direct messages to another user in a shared channels context.
In addition to user visibility, this evaluates remote-cluster direct-connect restrictions
for remote users.

__Minimum server version__: 10.11

##### Permissions
Must be authenticated and able to view the target user.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `other_user_id` | `string` | `path` | Yes | Other user GUID |

### Responses

#### 200 - DM permission check successful

Schema (application/json):
```json
{
  "can_dm": boolean, // Whether the user can send DMs to the other user
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

