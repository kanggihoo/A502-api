# 08-Receive a ping from a remote cluster. [POST]

`POST /api/v4/remotecluster/ping`

Receives heartbeat traffic from an already linked remote cluster.
This endpoint is authenticated with a remote-cluster token and is
used by the secure connection transport layer.

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

#### 200 - Ping response successful

Schema (application/json):
```json
{
  "sent_at": integer,
  "recv_at": integer,
}
```

#### 400 - 

#### 401 - 

