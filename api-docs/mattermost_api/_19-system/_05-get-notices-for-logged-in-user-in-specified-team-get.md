# 05-Get notices for logged in user in specified team [GET]

`GET /api/v4/system/notices/{team_id}`

Will return appropriate product notices for current user in the team specified by team_id parameter.
__Minimum server version__: 5.26
##### Permissions
Must be logged in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `clientVersion` | `string` | `query` | Yes | Version of the client (desktop/mobile/web) that issues the request |
| `locale` | `string` | `query` | No | Client locale |
| `client` | `string` | `query` | Yes | Client type (web/mobile-ios/mobile-android/desktop) |
| `team_id` | `string` | `path` | Yes | ID of the team |

### Responses

#### 200 - List notices retrieve successful

Schema (application/json):
```json
[
  {
    "id": string, // Notice ID
    "sysAdminOnly": boolean, // Does this notice apply only to sysadmins
    "teamAdminOnly": boolean, // Does this notice apply only to team admins
    "action": string, // Optional action to perform on action button click. (defaults to closing the notice)
    "actionParam": string, // Optional action parameter.  Example: {"action": "url", actionParam: "/console/some-page"}
    "actionText": string, // Optional override for the action button text (defaults to OK)
    "description": string, // Notice content. Use {{Mattermost}} instead of plain text to support white-labeling. Text supports Markdown.
    "image": string, // URL of image to display
    "title": string, // Notice title. Use {{Mattermost}} instead of plain text to support white-labeling. Text supports Markdown.
  }
]
```

#### 500 - 

