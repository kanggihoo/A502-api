# 35-Transfer a group [POST]

`POST /api/v4/groups/{id}/transfer`

Transfers a group to another parent group or transforms a subgroup into a top-level group. You must be an administrator or have the Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (application/json)

```json
{
  "group_id": integer, // The ID of the target group to which the group needs to be transferred to.If not provided, the source group will be promoted to a top-level group.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

