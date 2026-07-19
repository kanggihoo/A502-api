# 03-Get remote cluster info by ID for user. [GET]

`GET /api/v4/sharedchannels/remote_info/{remote_id}`

Get remote cluster info based on remoteId.

__Minimum server version__: 5.50

##### Permissions
Must be authenticated and user must belong to at least one channel shared with the remote cluster.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | Remote Cluster GUID |
| `include_deleted` | `boolean` | `query` | No | Include deleted remote clusters |

### Responses

#### 200 - Remote cluster info retrieval successful

Schema (application/json):
```json
{
  "display_name": string, // The display name for the remote cluster
  "create_at": integer, // The time in milliseconds a remote cluster was created
  "last_ping_at": integer, // The time in milliseconds a remote cluster was last pinged successfully
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

