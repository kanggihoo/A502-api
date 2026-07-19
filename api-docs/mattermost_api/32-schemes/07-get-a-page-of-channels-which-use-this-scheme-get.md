# 07-Get a page of channels which use this scheme. [GET]

`GET /api/v4/schemes/{scheme_id}/channels`

Get a page of channels which use this scheme. The provided Scheme ID should be for a Channel-scoped Scheme.
Use the query parameters to modify the behaviour of this endpoint.

##### Permissions
`manage_system` permission is required.

__Minimum server version__: 5.0


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scheme_id` | `string` | `path` | Yes | Scheme GUID |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of channels per page. |

### Responses

#### 200 - Channel list retrieval successful

Schema (application/json):
```json
[
  {
    "id": string,
    "create_at": integer, // The time in milliseconds a channel was created
    "update_at": integer, // The time in milliseconds a channel was last updated
    "delete_at": integer, // The time in milliseconds a channel was deleted
    "team_id": string,
    "type": string,
    "display_name": string,
    "name": string,
    "header": string,
    "purpose": string,
    "last_post_at": integer, // The time in milliseconds of the last post of a channel
    "total_msg_count": integer,
    "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
    "creator_id": string,
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

