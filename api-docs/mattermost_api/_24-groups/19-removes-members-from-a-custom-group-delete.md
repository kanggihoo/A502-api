# 19-Removes members from a custom group [DELETE]

`DELETE /api/v4/groups/{group_id}/members`

Soft deletes a custom group members.

##### Permissions
Must have `custom_group_manage_members` permission for the given group.

__Minimum server version__: 6.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | The ID of the group to delete. |

### Request Body (application/json)

```json
{
  "user_ids": [
    string
  ],
}
```
### Responses

#### 200 - Successfully deleted the group members.

Schema (application/json):
```json
[
  {
    "group_id": string,
    "user_id": string,
    "create_at": integer,
    "delete_at": integer,
  }
]
```

#### 403 - 

#### 404 - Can't find the group.

#### 501 - If the group does not have a `source` value of `custom`.

