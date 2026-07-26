# 14-Get the channels for a granular data retention policy [GET]

`GET /api/v4/data_retention/policies/{policy_id}/channels`

Gets the channels to which a granular data retention policy is applied.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the granular retention policy. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of channels per page. |

### Responses

#### 200 - Channels for retention policy successfully retrieved.

Schema (application/json):
```json
[
  any
]
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

