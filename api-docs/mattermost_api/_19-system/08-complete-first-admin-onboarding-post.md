# 08-Complete first admin onboarding [POST]

`POST /api/v4/system/onboarding/complete`

Mark first admin onboarding as complete and optionally trigger plugin installation.
##### Permissions Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "organization": string, // Organization name for self-hosted onboarding.
  "install_plugins": [
    string
  ], // Marketplace plugin IDs to install as part of onboarding.
}
```
### Responses

#### 200 - Onboarding completion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

