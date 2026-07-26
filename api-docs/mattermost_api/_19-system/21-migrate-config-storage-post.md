# 21-Migrate config storage [POST]

`POST /api/v4/config/migrate`

Migrate configuration between storage backends.
This endpoint is only exposed over a local socket.

##### Permissions
Must have `manage_system` permission.


### Request Body (application/json)

```json
{
  "from": string (required), // Source config store name.
  "to": string (required), // Destination config store name.
}
```
### Responses

#### 200 - Config migration successful

#### 400 - 

#### 403 - 

#### 500 - 

