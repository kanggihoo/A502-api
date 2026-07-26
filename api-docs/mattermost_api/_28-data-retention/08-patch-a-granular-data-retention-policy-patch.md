# 08-Patch a granular data retention policy [PATCH]

`PATCH /api/v4/data_retention/policies/{policy_id}`

Patches (i.e. replaces the fields of) a granular data retention policy.
If any fields are omitted, they will not be changed.

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
any
```
### Responses

#### 200 - Retention policy successfully patched.

Schema (application/json):
```json
any
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

