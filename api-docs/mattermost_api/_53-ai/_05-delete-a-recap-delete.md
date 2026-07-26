# 05-Delete a recap [DELETE]

`DELETE /api/v4/recaps/{recap_id}`

Delete a recap by its ID. Only the authenticated user who created the recap can delete it.
##### Permissions
Must be authenticated. Can only delete recaps created by the current user.
__Minimum server version__: 11.2


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `recap_id` | `string` | `path` | Yes | Recap GUID |

### Responses

#### 200 - Recap deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 404 - 

