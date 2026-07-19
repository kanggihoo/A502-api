# 08-Trigger notify-admin posts [POST]

`POST /api/v4/users/trigger-notify-admin-posts`

Trigger admin notification posts manually when enabled by configuration.
##### Permissions Must be authenticated and have `manage_system` permission.


### Request Body (application/json)

```json
{
  "trial_notification": boolean,
  "required_plan": string,
  "required_feature": string,
}
```
### Responses

#### 200 - Notify-admin posts triggered successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

