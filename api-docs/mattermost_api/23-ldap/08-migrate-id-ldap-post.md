# 08-Migrate Id LDAP [POST]

`POST /api/v4/ldap/migrateid`

Migrate LDAP IdAttribute to new value.
##### Permissions
Must have `manage_system` permission.
__Minimum server version__: 5.26


### Request Body (application/json)

```json
{
  "toAttribute": string (required), // New IdAttribute value
}
```
### Responses

#### 200 - Migration successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

