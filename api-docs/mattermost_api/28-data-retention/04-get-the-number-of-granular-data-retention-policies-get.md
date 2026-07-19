# 04-Get the number of granular data retention policies [GET]

`GET /api/v4/data_retention/policies_count`

Gets the number of granular (i.e. team or channel-specific) data retention
policies from the server.

__Minimum server version__: 5.35

##### Permissions
Must have the `sysconsole_read_compliance_data_retention` permission.

##### License
Requires an E20 license.


### Responses

#### 200 - Number of retention policies retrieved successfully.

Schema (application/json):
```json
{
  "total_count": integer, // The number of granular retention policies.
}
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

