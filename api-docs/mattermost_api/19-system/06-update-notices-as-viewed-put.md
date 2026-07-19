# 06-Update notices as 'viewed' [PUT]

`PUT /api/v4/system/notices/view`

Will mark the specified notices as 'viewed' by the logged in user.
__Minimum server version__: 5.26
##### Permissions
Must be logged in.


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Update successfull

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 500 - 

