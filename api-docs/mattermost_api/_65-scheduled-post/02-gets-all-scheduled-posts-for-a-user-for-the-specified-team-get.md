# 02-Gets all scheduled posts for a user for the specified team.. [GET]

`GET /api/v4/posts/scheduled/team/{team_id}`

Get user-team scheduled posts
##### Permissions
Must have `view_team` permission for the team the scheduled posts are being fetched for.
__Minimum server version__: 10.3


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `includeDirectChannels` | `boolean` | `query` | No | Whether to include scheduled posts from DMs an GMs or not. Default is false |

### Responses

#### 200 - Created scheduled post

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

