# 09-Get the system content flagging configuration [GET]

`GET /api/v4/content_flagging/config`

Returns the system configuration for content flagging, including settings related to notifications, flagging configurations, etc..
Only system admins can access this endpoint.


### Responses

#### 200 - Configuration retrieved successfully

Schema (application/json):
```json
{
  "EnableContentFlagging": boolean, // Flag to enable or disable content flagging feature
}
```

#### 403 - User does not have permission to manage system configuration.

#### 404 - Feature is disabled via the feature flag.

#### 500 - Internal server error.

