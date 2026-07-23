# 44-Attach mobile device and extra props to the session object [PUT]

`PUT /api/v4/users/sessions/device`

Attach extra props to the session object of the currently logged in session.
Adding a mobile device id will enable push notifications for a user, if configured by the server.
Other props are also available, like whether the device has notifications disabled and the mobile version.
##### Permissions
Must be authenticated.


### Request Body (application/json)

```json
{
  "device_id": string, // Mobile device id. For Android prefix the id with `android:` and Apple with `apple:`
  "voip_device_id": string, // VoIP push token. Same prefix shape as device_id. Optional; when provided, enables ring-style call push notifications.
  "deviceNotificationDisabled": string, // Whether the mobile device has notifications disabled. Accepted values are "true" or "false".
  "mobileVersion": string, // Mobile app version. The version must be parseable as a semver.
}
```
### Responses

#### 200 - Device id attach successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

