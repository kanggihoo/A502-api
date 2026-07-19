# 03-Get all IP filters [GET]

`GET /api/v4/ip_filtering/my_ip`

Retrieve your current IP address as seen by the workspace
__Minimum server version__: 9.1 __Note:__ This is intended for internal use and only applicable to Cloud workspaces


### Responses

#### 200 - IP address returned successfully

Schema (application/json):
```json
{
  "ip": string, // Your current IP address
}
```

#### 401 - 

#### 500 - 

#### 501 - 

