# 57-Revoke non-compliant personal access tokens [POST]

`POST /api/v4/users/tokens/non_compliant/revoke`

Revoke (hard-delete) every active personal access token that violates the configured `ServiceSettings.MaximumPersonalAccessTokenLifetimeDays` policy, along with any sessions created from them, and return the number of tokens revoked. Bot account tokens are exempt. The request is rejected with 400 when no maximum lifetime is configured, since there is nothing to revoke. This is irreversible; use `/users/tokens/non_compliant/count` first to preview the blast radius.

__Minimum server version__: 11.1

##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Non-compliant tokens revoked successfully

Schema (application/json):
```json
{
  "count": integer, // The number of personal access tokens revoked
}
```

#### 400 - 

#### 401 - 

#### 403 - 

