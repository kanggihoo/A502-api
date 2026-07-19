# 01-Upload audit log certificate [POST]

`POST /api/v4/audit_logs/certificate`

Upload the certificate to be used for TLS verification with the audit log service.

##### Permissions
Must have `sysconsole_write_experimental_features` permission.

__Minimum server version__: 10.9


### Request Body (multipart/form-data)

```json
{
  "certificate": string (required), // The certificate file
}
```
### Responses

#### 200 - Certificate upload successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 413 - 

#### 501 - 

