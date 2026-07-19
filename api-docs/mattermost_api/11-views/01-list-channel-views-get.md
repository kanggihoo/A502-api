# 01-List channel views [GET]

`GET /api/v4/channels/{channel_id}/views`

*__Experimental__: This endpoint is experimental and may change or be removed in a future release.*

Get a list of views for a channel.

__Minimum server version__: 11.6

##### Permissions
Must have `read_channel_content` permission for the channel.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel GUID |
| `per_page` | `integer` | `query` | No | The number of views per page (default 60, max 200) |
| `page` | `integer` | `query` | No | The 0-based page number for pagination (default 0) |
| `include_total_count` | `boolean` | `query` | No | When true, the response is a ViewsWithCount object containing a views array and a total_count integer. When false or omitted, the response is a plain JSON array of View objects.<br> |

### Responses

#### 200 - Channel views retrieval successful

Schema (application/json):
```json
any
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

