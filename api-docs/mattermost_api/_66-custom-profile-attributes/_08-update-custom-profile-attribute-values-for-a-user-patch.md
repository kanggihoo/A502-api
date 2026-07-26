# 08-Update custom profile attribute values for a user [PATCH]

`PATCH /api/v4/users/{user_id}/custom_profile_attributes`

Update Custom Profile Attribute field values for a specific user.

**Note:** Values for fields with `attrs.protected = true` cannot be
updated and will return an error.

__Minimum server version__: 11

##### Permissions
Must have permission to edit the user. Users can only edit their own CPA values unless they are system administrators.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
[
  {
    "id": string,
    "value": any,
  }
]
```
### Responses

#### 200 - Custom profile attribute values updated successfully

Schema (application/json):
```json
[
  {
    "id": string,
    "value": any,
  }
]
```

#### 400 - 

#### 403 - 

#### 404 - 

