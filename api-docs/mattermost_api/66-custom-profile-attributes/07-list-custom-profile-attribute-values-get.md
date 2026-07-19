# 07-List Custom Profile Attribute values [GET]

`GET /api/v4/users/{user_id}/custom_profile_attributes`

List all the Custom Profile Attributes values for specified user.

__Minimum server version__: 10.5

##### Permissions
Must have `view members` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - Custom Profile Attribute values fetch successful. Result may be empty.

#### 400 - 

#### 401 - 

#### 403 - 

