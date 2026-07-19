# 44-Get an image by url [GET]

`GET /api/v4/image`

Fetches an image via Mattermost image proxy.
__Minimum server version__: 3.10
##### Permissions
Must be logged in.


### Responses

#### 200 - Image found

Schema (image/*):
```json
string
```

#### 404 - 

