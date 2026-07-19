# 02-Get all IP filters [POST]

`POST /api/v4/ip_filtering`

Adjust IP Filters applied to the workspace
__Minimum server version__: 9.1 __Note:__ This is intended for internal use and only applicable to Cloud workspaces


### Request Body (application/json)

```json
[
  {
    "CIDRBlock": string, // An IP address range in CIDR notation
    "Description": string, // A description for the CIDRBlock
  }
]
```
### Responses

#### 200 - IP Filters returned successfully

Schema (application/json):
```json
[
  {
    "CIDRBlock": string, // An IP address range in CIDR notation
    "Description": string, // A description for the CIDRBlock
  }
]
```

#### 401 - 

#### 500 - 

#### 501 - 

