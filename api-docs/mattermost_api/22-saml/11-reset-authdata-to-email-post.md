# 11-Reset AuthData to Email [POST]

`POST /api/v4/saml/reset_auth_data`

Reset the AuthData field of SAML users to their email. This is meant to be used when the "id" attribute is set to an empty value ("") from a previously non-empty value.
__Minimum server version__: 5.35
##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "include_deleted": boolean, // Whether to include deleted users.
  "dry_run": boolean, // If set to true, the number of users who would be affected is returned.
  "user_ids": [
    string
  ], // If set to a non-empty array, then users whose IDs are not in the array will be excluded.
}
```
### Responses

#### 200 - AuthData successfully reset

Schema (application/json):
```json
{
  "num_affected": integer, // The number of users whose AuthData field was reset.
}
```

#### 403 - 

#### 501 - 

