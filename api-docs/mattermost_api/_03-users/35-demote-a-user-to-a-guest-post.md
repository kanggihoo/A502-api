# 35-Demote a user to a guest [POST]

`POST /api/v4/users/{user_id}/demote`

Convert a regular user into a guest. This will convert the user into a
guest for the whole system while retaining their existing team and
channel memberships.

__Minimum server version__: 5.16

##### Permissions
Must be logged in as the user or have the `demote_to_guest` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User successfully demoted

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

