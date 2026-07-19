# 15-Checks the validity of a Site URL [POST]

`POST /api/v4/site_url/test`

Sends a Ping request to the mattermost server using the specified Site URL.

##### Permissions
Must have `manage_system` permission.

__Minimum server version__: 5.16


### Request Body (application/json)

```json
{
  "site_url": string (required), // The Site URL to test
}
```
### Responses

#### 200 - Site URL is valid

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 403 - 

#### 500 - 

