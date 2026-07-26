# 33-Invalidate all the caches [POST]

`POST /api/v4/caches/invalidate`

Purge all the in-memory caches for the Mattermost server. This can have a temporary negative effect on performance while the caches are re-populated.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - Caches invalidate successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 403 - 

