# 10-Get authorized OAuth apps [GET]

`GET /api/v4/users/{user_id}/oauth/apps/authorized`

Get a page of OAuth 2.0 client applications authorized to access a user's account.
##### Permissions
Must be authenticated as the user or have `edit_other_users` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
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

