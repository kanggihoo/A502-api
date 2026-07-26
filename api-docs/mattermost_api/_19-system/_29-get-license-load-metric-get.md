# 29-Get license load metric [GET]

`GET /api/v4/license/load_metric`

Get the current license load metric, calculated based on monthly active users against the licensed user count. Returns a value of 0 when there is no license loaded or the license doesn't have a user count.
__Minimum server version__: 10.8
##### Permissions
Must be logged in.


### Responses

#### 200 - License load metric retrieval successful

Schema (application/json):
```json
{
  "load": integer, // Current license load metric as an integer
}
```

#### 401 - 

#### 500 - 

