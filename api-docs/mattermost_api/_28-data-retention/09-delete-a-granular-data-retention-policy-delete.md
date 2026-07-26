# 09-Delete a granular data retention policy [DELETE]

`DELETE /api/v4/data_retention/policies/{policy_id}`

Deletes a granular data retention policy.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_write_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |

### Responses

#### 200 - Retention policy successfully deleted.

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

