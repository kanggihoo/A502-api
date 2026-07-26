# 04-Delete a Custom Profile Attribute field [DELETE]

`DELETE /api/v4/custom_profile_attributes/fields/{field_id}`

Marks a Custom Profile Attribute field and all its values as
deleted.

__Minimum server version__: 10.5

##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `field_id` | `string` | `path` | Yes | Custom Profile Attribute field GUID |

### Responses

#### 200 - Custom Profile Attribute field deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

