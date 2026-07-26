# 03-Get an OAuth app [GET]

`GET /api/v4/oauth/apps/{app_id}`

Get an OAuth 2.0 client application registered with Mattermost.
##### Permissions
If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `app_id` | `string` | `path` | Yes | Application client id |

### Responses

#### 200 - App retrieval successful

Schema (application/json):
```json
{
  "id": string, // The client id of the application
  "client_secret": string, // The client secret of the application
  "name": string, // The name of the client application
  "description": string, // A short description of the application
  "icon_url": string, // A URL to an icon to display with the application
  "callback_urls": [
    string
  ], // A list of callback URLs for the appliation
  "homepage": string, // A link to the website of the application
  "is_trusted": boolean, // Set this to `true` to skip asking users for permission
  "create_at": integer, // The time of registration for the application
  "update_at": integer, // The last time of update for the application
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 501 - 

