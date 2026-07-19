# 01-Retrieve a list of supported timezones [GET]

`GET /api/v4/system/timezones`

__Minimum server version__: 3.10
##### Permissions
Must be logged in.


### Responses

#### 200 - List of timezones retrieval successful

Schema (application/json):
```json
[
  string
]
```

#### 500 - 

