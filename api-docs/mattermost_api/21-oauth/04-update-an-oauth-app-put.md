# 04-Update an OAuth app [PUT]

`PUT /api/v4/oauth/apps/{app_id}`

Update an OAuth 2.0 client application based on OAuth struct.
##### Permissions
If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `app_id` | `string` | `path` | Yes | Application client id |

### Request Body (application/json)

```json
{
  "id": string (required), // The id of the client application
  "name": string (required), // The name of the client application
  "description": string (required), // A short description of the application
  "icon_url": string, // A URL to an icon to display with the application
  "callback_urls": [
    string
  ] (required), // A list of callback URLs for the appliation
  "homepage": string (required), // A link to the website of the application
  "is_trusted": boolean, // Set this to `true` to skip asking users for permission. It will be set to false if value is not provided.
}
```
### Responses

#### 200 - App update successful

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

