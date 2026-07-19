# 07-Validate workspace business email [POST]

`POST /api/v4/cloud/validate-workspace-business-email`

Validate the current workspace customer/admin email as a business email.
##### Permissions Must have `sysconsole_write_billing` permission and be licensed for Cloud.


### Responses

#### 200 - Workspace email validation successful

Schema (application/json):
```json
{
  "is_valid": boolean,
}
```

#### 401 - 

#### 403 - 

#### 501 - 

