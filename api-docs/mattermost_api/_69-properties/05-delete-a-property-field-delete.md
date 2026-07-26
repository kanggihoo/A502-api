# 05-Delete a property field [DELETE]

`DELETE /api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}`

Deletes a property field and all its associated values. Returns 409 Conflict if the field has active linked dependents; unlink or delete dependent fields first.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_name` | `string` | `path` | Yes | The name of the property group |
| `object_type` | `string` | `path` | Yes | The type of object this property field applies to |
| `field_id` | `string` | `path` | Yes | Property field ID |

### Responses

#### 200 - Property field deletion successful

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

#### 409 - The field has active linked dependents. Unlink or delete dependent fields before deleting the source.


