# 04-Creates a new terms of service [POST]

`POST /api/v4/terms_of_service`

Creates new terms of service

__Minimum server version__: 5.4
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - terms of service fetched successfully

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

