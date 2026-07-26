# 10-Get certificate status [GET]

`GET /api/v4/saml/certificate/status`

Get the status of the uploaded certificates and keys in use by your SAML configuration.
##### Permissions
Must have `sysconsole_write_authentication` permission.


### Responses

#### 200 - SAML certificate status retrieval successful

Schema (application/json):
```json
{
  "idp_certificate_file": boolean, // Status is good when `true`
  "public_certificate_file": boolean, // Status is good when `true`
  "private_key_file": boolean, // Status is good when `true`
}
```

#### 403 - 

#### 501 - 

