# 09-Receive a remote cluster message. [POST]

`POST /api/v4/remotecluster/msg`

Receives and processes an incoming transport message from a linked
remote cluster. This endpoint is authenticated with a remote-cluster
token and is part of the secure connection protocol.

##### Permissions
No user session permissions required.


### Request Body (application/json)

```json
{
  "remote_id": string,
  "msg": {
    "id": string,
    "topic": string,
    "create_at": integer,
    "payload": {}, // Raw message payload.
  },
}
```
### Responses

#### 200 - Message accepted successfully

Schema (application/json):
```json
{
  "status": string,
  "err": string,
  "payload": {}, // Raw response payload.
}
```

#### 400 - 

#### 401 - 

