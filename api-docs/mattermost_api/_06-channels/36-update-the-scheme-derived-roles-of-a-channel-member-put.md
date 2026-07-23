# 36-Update the scheme-derived roles of a channel member. [PUT]

`PUT /api/v4/channels/{channel_id}/members/{user_id}/schemeRoles`

Update a channel member's scheme_admin/scheme_user properties. Typically this should either be `scheme_admin=false, scheme_user=true` for ordinary channel member, or `scheme_admin=true, scheme_user=true` for a channel admin.
__Minimum server version__: 5.0
##### Permissions
Must be authenticated and have the `manage_channel_roles` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "scheme_admin": boolean (required),
  "scheme_user": boolean (required),
}
```
### Responses

#### 200 - Channel member's scheme-derived roles updated successfully.

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

