# 15-Get access control attributes for a channel [GET]

`GET /api/v4/channels/{channel_id}/access_control/attributes`

Retrieves the effective access control policy attributes for a specific channel.
This can be used to understand what attributes are currently being applied to the channel by the access control system.
##### Permissions
Must have `read_channel` permission for the specified channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | The ID of the channel. |

### Responses

#### 200 - Access control attributes retrieved successfully.

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

