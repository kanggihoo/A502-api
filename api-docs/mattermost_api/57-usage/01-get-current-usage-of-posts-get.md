# 01-Get current usage of posts [GET]

`GET /api/v4/usage/posts`

Retrieve rounded off total no. of posts for this instance. Example: returns 4000 instead of 4321
##### Permissions
Must be authenticated.
__Minimum server version__: 7.0


### Responses

#### 200 - Total no. of posts returned successfully

Schema (application/json):
```json
{
  "count": number, // Total no. of posts
}
```

#### 401 - 

#### 500 - 

