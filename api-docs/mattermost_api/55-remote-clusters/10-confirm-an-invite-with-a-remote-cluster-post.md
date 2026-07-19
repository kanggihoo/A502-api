# 10-Confirm an invite with a remote cluster. [POST]

`POST /api/v4/remotecluster/confirm_invite`

Confirms an invitation handshake from a linked remote cluster.
This endpoint is authenticated with a remote-cluster token and is
used by the secure connection protocol.

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

#### 200 - Invitation confirmation successful

#### 400 - 

#### 401 - 

