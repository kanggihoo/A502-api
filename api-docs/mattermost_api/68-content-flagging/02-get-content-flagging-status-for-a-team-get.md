# 02-Get content flagging status for a team [GET]

`GET /api/v4/content_flagging/team/{team_id}/status`

Returns the content flagging status for a specific team, indicating whether content flagging is enabled on the specified team or not.
An enterprise advanced license is required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | The ID of the team to retrieve the content flagging status for |

### Responses

#### 200 - Content flagging status retrieved successfully

Schema (application/json):
```json
{
  "enabled": boolean, // Indicates if content flagging is enabled for the team
}
```

#### 403 - Forbidden - User does not have permission to access this team.

#### 404 - The specified team was not found or the feature is disabled via the feature flag.

#### 500 - Internal server error.

#### 501 - Feature is disabled either via config or an Enterprise Advanced license is not available.

