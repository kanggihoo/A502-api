# 11-Upload private key [POST]

`POST /api/v4/ldap/certificate/private`

Upload the private key to be used for TLS verification. The server will pick a hard-coded filename for the PrivateKeyFile setting in your `config.json`.
##### Permissions
Must have `manage_system` permission.


### Request Body (multipart/form-data)

```json
{
  "certificate": string (required), // The private key file
}
```
### Responses

#### 200 - LDAP certificate upload successful

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

