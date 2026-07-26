# 06-Upload public certificate [POST]

`POST /api/v4/saml/certificate/public`

Upload the public certificate to be used for encryption with your SAML configuration. The server will pick a hard-coded filename for the PublicCertificateFile setting in your `config.json`.
##### Permissions
Must have `sysconsole_write_authentication` permission.


### Request Body (multipart/form-data)

```json
{
  "certificate": string (required), // The public certificate file
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

