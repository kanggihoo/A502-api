# 56-Count non-compliant personal access tokens [GET]

`GET /api/v4/users/tokens/non_compliant/count`

Count the active personal access tokens that violate the configured `ServiceSettings.MaximumPersonalAccessTokenLifetimeDays` policy (tokens that never expire or expire beyond the cap). Bot account tokens are exempt and never counted. Returns 0 when no maximum lifetime is configured.

__Minimum server version__: 11.1

##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Count retrieved successfully

Schema (application/json):
```json
{
  "count": integer, // The number of non-compliant personal access tokens
}
```

#### 401 - 

#### 403 - 

