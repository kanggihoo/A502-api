# 01-Get cloud workspace limits [GET]

`GET /api/v4/cloud/limits`

Retrieve any cloud workspace limits applicable to this instance.
##### Permissions
Must be authenticated and be licensed for Cloud.
__Minimum server version__: 7.0 __Note:__ This is intended for internal use and is subject to change.


### Responses

#### 200 - Cloud workspace limits returned successfully

Schema (application/json):
```json
{
  "boards": any,
  "files": any,
  "integrations": any,
  "messages": any,
  "teams": any,
}
```

#### 401 - 

#### 500 - 

#### 501 - 

