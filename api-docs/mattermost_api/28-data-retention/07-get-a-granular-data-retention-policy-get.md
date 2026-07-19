# 07-Get a granular data retention policy [GET]

`GET /api/v4/data_retention/policies/{policy_id}`

Gets details about a granular data retention policies by ID.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |

### Responses

#### 200 - Retention policy's details retrieved successfully.

Schema (application/json):
```json
any
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

