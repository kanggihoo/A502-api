# 03-Create a custom group [POST]

`POST /api/v4/groups`

Create a `custom` type group.

#### Permission
Must have `create_custom_group` permission.

__Minimum server version__: 6.3


### Request Body (application/json)

```json
{
  "name": string (required), // The unique group name used for at-mentioning.
  "display_name": string (required), // The display name of the group which can include spaces.
  "source": string (required), // Must be `custom`
  "allow_reference": boolean (required), // Must be true
  "user_ids": [
    string
  ] (required), // The user ids of the group members to add.
}
```
### Responses

#### 201 - Group creation and memberships successful.

#### 400 - 

#### 403 - 

#### 501 - Group has an invalid `source`, or
`allow_reference` is not `true`, or
group has a `remote_id`.


