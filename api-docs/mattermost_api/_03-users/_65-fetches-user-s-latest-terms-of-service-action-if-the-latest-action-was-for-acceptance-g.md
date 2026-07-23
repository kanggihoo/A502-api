# 65-Fetches user's latest terms of service action if the latest action was for acceptance. [GET]

`GET /api/v4/users/{user_id}/terms_of_service`

Will be deprecated in v6.0
Fetches user's latest terms of service action if the latest action was for acceptance.

__Minimum server version__: 5.6
##### Permissions
Must be logged in as the user being acted on.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Responses

#### 200 - User's accepted terms of service action

Schema (application/json):
```json
{
  "user_id": string, // The unique identifier of the user who performed this terms of service action.
  "terms_of_service_id": string, // The unique identifier of the terms of service the action was performed on.
  "create_at": integer, // The time in milliseconds that this action was performed.
}
```

#### 400 - 

#### 401 - 

#### 404 - User hasn't performed an action or the latest action was a rejection.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

