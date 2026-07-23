# 36-Promote a guest to user [POST]

`POST /api/v4/users/{user_id}/promote`

Convert a guest into a regular user. This will convert the guest into a
user for the whole system while retaining any team and channel
memberships and automatically joining them to the default channels.

__Minimum server version__: 5.16

##### Permissions
Must be logged in as the user or have the `promote_guest` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Guest successfully promoted

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

