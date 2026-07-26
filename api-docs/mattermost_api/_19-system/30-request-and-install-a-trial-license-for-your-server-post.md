# 30-Request and install a trial license for your server [POST]

`POST /api/v4/trial-license`

Request and install a trial license for your server
__Minimum server version__: 5.25
##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "users": integer (required), // Number of users requested (20% extra is going to be added)
}
```
### Responses

#### 200 - Trial license obtained and installed

#### 400 - 

#### 401 - 

#### 403 - 

