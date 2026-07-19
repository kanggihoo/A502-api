# 16-Delete channels from a granular data retention policy [DELETE]

`DELETE /api/v4/data_retention/policies/{policy_id}/channels`

Delete channels from a granular data retention policy.

 __Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_write_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |

### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Channels successfully deleted from retention policy.

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

