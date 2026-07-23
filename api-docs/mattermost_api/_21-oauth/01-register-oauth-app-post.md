# 01-Register OAuth app [POST]

`POST /api/v4/oauth/apps`

Register an OAuth 2.0 client application with Mattermost as the service provider.
##### Permissions
Must have `manage_oauth` permission.


### Request Body (application/json)

```json
{
  "name": string (required), // The name of the client application
  "description": string (required), // A short description of the application
  "icon_url": string, // A URL to an icon to display with the application
  "callback_urls": [
    string
  ] (required), // A list of callback URLs for the appliation
  "homepage": string (required), // A link to the website of the application
  "is_trusted": boolean, // Set this to `true` to skip asking users for permission
  "is_public": boolean, // Set this to `true` to create a public client (no client secret). Public clients must use PKCE for authorization.
}
```
### Responses

#### 201 - App registration successful

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

#### 501 - 

