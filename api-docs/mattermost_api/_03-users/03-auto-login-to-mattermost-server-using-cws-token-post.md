# 03-Auto-Login to Mattermost server using CWS token [POST]

`POST /api/v4/users/login/cws`

CWS stands for Customer Web Server which is the cloud service used to manage cloud instances.
##### Permissions
A Cloud license is required


### Request Body (application/json)

```json
{
  "login_id": string,
  "cws_token": string,
}
```
### Responses

#### 302 - Login successful, it'll redirect to login page to perform the autologin

#### 400 - 

#### 401 - 

#### 403 - 

