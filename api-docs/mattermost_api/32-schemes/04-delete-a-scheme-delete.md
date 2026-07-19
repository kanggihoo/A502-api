# 04-Delete a scheme [DELETE]

`DELETE /api/v4/schemes/{scheme_id}`

Soft deletes a scheme, by marking the scheme as deleted in the database.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scheme_id` | `string` | `path` | Yes | ID of the scheme to delete |

### Responses

#### 200 - Scheme deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

