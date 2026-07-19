# 64-Records user action when they accept or decline custom terms of service [POST]

`POST /api/v4/users/{user_id}/terms_of_service`

Records user action when they accept or decline custom terms of service. Records the action in audit table.
Updates user's last accepted terms of service ID if they accepted it.

__Minimum server version__: 5.4
##### Permissions
Must be logged in as the user being acted on.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "serviceTermsId": string (required), // terms of service ID on which the user is acting on
  "accepted": string (required), // true or false, indicates whether the user accepted or rejected the terms of service.
}
```
### Responses

#### 200 - Terms of service action recorded successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

