# 02-Remove audit log certificate [DELETE]

`DELETE /api/v4/audit_logs/certificate`

Delete the current certificate being used with the audit log service.

##### Permissions
Must have `sysconsole_write_experimental_features` permission.

__Minimum server version__: 9.5


### Responses

#### 200 - Certificate deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 401 - 

#### 403 - 

#### 501 - 

