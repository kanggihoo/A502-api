# 09-Delete an access control policy [DELETE]

`DELETE /api/v4/access_control_policies/{policy_id}`

Deletes an access control policy by its ID.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |

### Responses

#### 200 - Access control policy deleted successfully.

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

#### 500 - 

