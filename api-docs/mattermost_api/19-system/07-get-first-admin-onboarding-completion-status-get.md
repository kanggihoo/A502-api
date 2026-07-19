# 07-Get first admin onboarding completion status [GET]

`GET /api/v4/system/onboarding/complete`

Get whether first admin onboarding is complete.
##### Permissions Must have `manage_system` permission.


### Responses

#### 200 - Onboarding completion state retrieval successful

Schema (application/json):
```json
{
  "name": string, // System property name
  "value": string, // System property value
}
```

#### 401 - 

#### 403 - 

#### 500 - 

