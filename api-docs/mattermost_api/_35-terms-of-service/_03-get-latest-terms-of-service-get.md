# 03-Get latest terms of service [GET]

`GET /api/v4/terms_of_service`

Get latest terms of service from the server

__Minimum server version__: 5.4
##### Permissions
Must be authenticated.


### Responses

#### 200 - Terms of service fetched successfully

Schema (application/json):
```json
{
  "id": string, // The unique identifier of the terms of service.
  "create_at": integer, // The time at which the terms of service was created.
  "user_id": string, // The unique identifier of the user who created these terms of service.
  "text": string, // The text of terms of service. Supports Markdown.
}
```

#### 400 - 

#### 401 - 

