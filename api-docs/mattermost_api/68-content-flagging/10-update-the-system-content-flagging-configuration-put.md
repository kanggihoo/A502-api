# 10-Update the system content flagging configuration [PUT]

`PUT /api/v4/content_flagging/config`

Updates the system configuration for content flagging, including settings related to notifications, flagging configurations, etc..
Only system admins can access this endpoint.


### Request Body (application/json)

```json
{
  "EnableContentFlagging": boolean, // Flag to enable or disable content flagging feature
}
```
### Responses

#### 200 - Configuration updated successfully

#### 400 - Bad request - Invalid input data or missing required fields.

#### 403 - User does not have permission to manage system configuration.

#### 404 - Feature is disabled via the feature flag.

#### 500 - Internal server error.

