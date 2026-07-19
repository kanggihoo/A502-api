# 02-Create channel view [POST]

`POST /api/v4/channels/{channel_id}/views`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Create a new view for a channel.

__Minimum server version__: 11.6

##### Permissions
Must have `create_post` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the view
  "type": enum("kanban") (required), // The type of the view. * `kanban` - a kanban view 
  "description": string, // The description of the view
  "sort_order": integer, // The display order of the view within the channel
  "props": {}, // Arbitrary key-value properties for the view
}
```
### Responses

#### 201 - Channel view creation successful

Schema (application/json):
```json
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
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

