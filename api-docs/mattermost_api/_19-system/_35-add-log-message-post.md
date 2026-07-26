# 35-Add log message [POST]

`POST /api/v4/logs`

Add log messages to the server logs.
##### Permissions
Users with `manage_system` permission can log ERROR or DEBUG messages.
Logged in users can log ERROR or DEBUG messages when `ServiceSettings.EnableDeveloper` is `true` or just DEBUG messages when `false`.
Non-logged in users can log ERROR or DEBUG messages when `ServiceSettings.EnableDeveloper` is `true` and cannot log when `false`.


### Request Body (application/json)

```json
{
  "level": string (required), // The error level, ERROR or DEBUG
  "message": string (required), // Message to send to the server logs
}
```
### Responses

#### 200 - Logs sent successful

Schema (application/json):
```json
{}
```

#### 403 - 

