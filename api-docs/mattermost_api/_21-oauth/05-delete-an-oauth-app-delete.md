# 05-Delete an OAuth app [DELETE]

`DELETE /api/v4/oauth/apps/{app_id}`

Delete and unregister an OAuth 2.0 client application 
##### Permissions
If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `app_id` | `string` | `path` | Yes | Application client id |

### Responses

#### 200 - App deletion successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

