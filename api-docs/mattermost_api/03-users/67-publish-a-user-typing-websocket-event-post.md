# 67-Publish a user typing websocket event. [POST]

`POST /api/v4/users/{user_id}/typing`

Notify users in the given channel via websocket that the given user is typing.
__Minimum server version__: 5.26
##### Permissions
Must have `manage_system` permission to publish for any user other than oneself.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |

### Request Body (application/json)

```json
{
  "channel_id": string (required), // The id of the channel to which to direct the typing event.
  "parent_id": string, // The optional id of the root post of the thread to which the user is replying. If unset, the typing event is directed at the entire channel.
}
```
### Responses

#### 200 - User typing websocket event accepted for publishing.

#### 400 - 

#### 401 - 

#### 403 - 

