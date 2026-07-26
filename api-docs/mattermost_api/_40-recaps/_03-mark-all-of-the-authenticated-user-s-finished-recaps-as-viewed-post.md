# 03-Mark all of the authenticated user's finished recaps as viewed [POST]

`POST /api/v4/recaps/mark_viewed`

Mark every not-yet-viewed completed or failed recap belonging to the authenticated user as viewed at the current time. Pending and processing recaps are not affected. Returns the IDs of the recaps that were updated. The server broadcasts a `recap_updated` WebSocket event for each affected recap.
Typically called once when the recaps page is opened so the sidebar unread badge can be cleared in bulk.
##### Permissions
Must be authenticated. Operates only on the authenticated user's own recaps.
__Minimum server version__: 11.2


### Responses

#### 200 - Recaps marked as viewed successfully

Schema (application/json):
```json
{
  "recap_ids": [
    string
  ], // IDs of the recaps that were updated
}
```

#### 401 - 

#### 501 - AI Recaps feature flag is disabled

