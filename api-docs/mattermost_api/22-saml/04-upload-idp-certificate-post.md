# 04-Upload IDP certificate [POST]

`POST /api/v4/saml/certificate/idp`

Upload the IDP certificate to be used with your SAML configuration. The server will pick a hard-coded filename for the IdpCertificateFile setting in your `config.json`.
##### Permissions
Must have `sysconsole_write_authentication` permission.


### Request Body (multipart/form-data)

```json
{
  "certificate": string (required), // The IDP certificate file
}
```
### Responses

#### 200 - SAML certificate upload successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

