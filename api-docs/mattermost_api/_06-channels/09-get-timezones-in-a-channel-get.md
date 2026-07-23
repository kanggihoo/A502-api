# 09-Get timezones in a channel [GET]

`GET /api/v4/channels/{channel_id}/timezones`

Get a list of timezones for the users who are in this channel.

__Minimum server version__: 5.6

##### Permissions
Must have the `read_channel` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |

### Responses

#### 200 - Timezone retrieval successful

Schema (application/json):
```json
[
  string
]
```

#### 400 - 

#### 401 - 

#### 403 - 

