# 02-Get OAuth apps [GET]

`GET /api/v4/oauth/apps`

Get a page of OAuth 2.0 client applications registered with Mattermost.
##### Permissions
With `manage_oauth` permission, the apps registered by the logged in user are returned. With `manage_system_wide_oauth` permission, all apps regardless of creator are returned.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of apps per page. |

### Responses

#### 200 - OAuthApp list retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

