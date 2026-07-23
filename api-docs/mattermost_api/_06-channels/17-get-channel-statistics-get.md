# 17-Get channel statistics [GET]

`GET /api/v4/channels/{channel_id}/stats`

Get statistics for a channel.
##### Permissions
Must have the `read_channel` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Channel statistics retrieval successful

Schema (application/json):
```json
{
  "channel_id": string,
  "member_count": integer,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

