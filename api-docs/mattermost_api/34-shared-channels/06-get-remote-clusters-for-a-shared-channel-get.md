# 06-Get remote clusters for a shared channel [GET]

`GET /api/v4/sharedchannels/{channel_id}/remotes`

Gets the remote clusters information for a shared channel.

__Minimum server version__: 10.11

##### Permissions
Must be authenticated and have the `read_channel` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Remote clusters retrieval successful

Schema (application/json):
```json
[
  {
    "display_name": string, // The display name for the remote cluster
    "create_at": integer, // The time in milliseconds a remote cluster was created
    "last_ping_at": integer, // The time in milliseconds a remote cluster was last pinged successfully
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

