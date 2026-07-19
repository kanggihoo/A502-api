# 46-Get the current status for the inplace upgrade from Team Edition to Enterprise Edition [GET]

`GET /api/v4/upgrade_to_enterprise/status`

It returns the percentage of completion of the current upgrade or the error if there is any.
__Minimum server version__: 5.27
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Upgrade status

Schema (application/json):
```json
{
  "percentage": integer, // Current percentage of the upgrade
  "error": string, // Error happened during the upgrade
}
```

#### 403 - 

