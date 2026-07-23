# 05-Deletes a custom group [DELETE]

`DELETE /api/v4/groups/{group_id}`

Soft deletes a custom group.

##### Permissions
Must have `custom_group_delete` permission for the given group.

__Minimum server version__: 6.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_id` | `string` | `path` | Yes | The ID of the group. |

### Responses

#### 200 - Successfully deleted the group.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

#### 404 - Group is already deleted or doesn't exist.

#### 501 - The group doesn't have a `source` value of `custom`.

