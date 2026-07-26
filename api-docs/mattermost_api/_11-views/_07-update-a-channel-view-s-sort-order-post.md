# 07-Update a channel view's sort order [POST]

`POST /api/v4/channels/{channel_id}/views/{view_id}/sort_order`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Updates the sort order of a channel view, setting its new index
from the request body and updating the rest of the views in the
channel to accommodate the change.

__Minimum server version__: 11.6

##### Permissions
Must have `create_post` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `view_id` | `string` | `path` | Yes | View GUID |

### Request Body (application/json)

```json
integer
```
### Responses

#### 200 - Channel view sort order update successful

Schema (application/json):
```json
[
  {
    "id": string, // The unique identifier of the view
    "channel_id": string, // The ID of the channel this view belongs to
    "type": enum("kanban"),
    "creator_id": string, // The ID of the user who created this view
    "title": string, // The title of the view
    "description": string, // The description of the view
    "sort_order": integer, // The display order of the view within the channel
    "props": {}, // Arbitrary key-value properties for the view
    "create_at": integer, // The time in milliseconds the view was created
    "update_at": integer, // The time in milliseconds the view was last updated
    "delete_at": integer, // The time in milliseconds the view was deleted
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

