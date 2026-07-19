# 05-Get the granular data retention policies [GET]

`GET /api/v4/data_retention/policies`

Gets details about the granular (i.e. team or channel-specific) data retention
policies from the server.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of policies per page. |

### Responses

#### 200 - Retention policies' details retrieved successfully.

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

