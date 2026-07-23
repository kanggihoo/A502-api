# 07-Save notify-admin intent [POST]

`POST /api/v4/users/notify-admin`

Save a notify-admin request for upgrade or trial flows.
##### Permissions Must be authenticated.


### Request Body (application/json)

```json
{
  "trial_notification": boolean,
  "required_plan": string,
  "required_feature": string,
}
```
### Responses

#### 200 - Notify-admin request saved

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

