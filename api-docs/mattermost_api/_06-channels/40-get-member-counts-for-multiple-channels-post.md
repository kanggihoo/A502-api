# 40-Get member counts for multiple channels [POST]

`POST /api/v4/channels/stats/member_count`

Get channel member counts for a list of channel IDs.
##### Permissions
Must have access to member count for all requested channels.


### Request Body (application/json)

```json
[
  string
]
```
### Responses

#### 200 - Channel member counts retrieval successful

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

