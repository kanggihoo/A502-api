# 02-Get shared channel remotes by remote cluster. [GET]

`GET /api/v4/remotecluster/{remote_id}/sharedchannelremotes`

Get a list of the channels shared with a given remote cluster
and their status.

##### Permissions
`manage_secure_connections` or `manage_shared_channels`


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `remote_id` | `string` | `path` | Yes | The remote cluster GUID |
| `include_unconfirmed` | `boolean` | `query` | No | Include those Shared channel remotes that are unconfirmed |
| `exclude_confirmed` | `boolean` | `query` | No | Show only those Shared channel remotes that are not confirmed yet |
| `exclude_home` | `boolean` | `query` | No | Show only those Shared channel remotes that were shared with this server |
| `exclude_remote` | `boolean` | `query` | No | Show only those Shared channel remotes that were shared from this server |
| `include_deleted` | `boolean` | `query` | No | Include those Shared channel remotes that have been deleted |
| `page` | `integer` | `query` | No | The page to select |
| `per_page` | `integer` | `query` | No | The number of shared channels per page |

### Responses

#### 200 - Shared channel remotes fetch successful. Result might be empty.

Schema (application/json):
```json
[
  {
    "id": string, // The id of the shared channel remote
    "channel_id": string, // The id of the channel
    "creator_id": string, // Id of the user that invited the remote to share the channel
    "create_at": integer, // Time in milliseconds that the remote was invited to the channel
    "update_at": integer, // Time in milliseconds that the shared channel remote record was last updated
    "delete_at": integer, // Time in milliseconds that the shared chanenl remote record was deleted
    "is_invite_accepted": boolean, // Indicates if the invite has been accepted by the remote
    "is_invite_confirmed": boolean, // Indicates if the invite has been confirmed by the remote
    "remote_id": string, // Id of the remote cluster that the channel is shared with
    "last_post_update_at": integer, // Time in milliseconds of the last post in the channel that was synchronized with the remote update_at
    "last_post_id": string, // Id of the last post in the channel that was synchronized with the remote
    "last_post_create_at": string, // Time in milliseconds of the last post in the channel that was synchronized with the remote create_at
    "last_post_create_id": string,
  }
]
```

#### 401 - 

#### 403 - 

