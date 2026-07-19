# 13-Get channels for an access control policy [GET]

`GET /api/v4/access_control_policies/{policy_id}/resources/channels`

Retrieves a paginated list of channels to which a specific access control policy is applied.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |
| `after` | `string` | `query` | No | The channel ID to start after for pagination. |
| `limit` | `integer` | `query` | Yes | The maximum number of channels to return. |

### Responses

#### 200 - Channels retrieved successfully.

Schema (application/json):
```json
{
  "channels": [
    any
  ],
  "total_count": integer, // The total number of channels.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

#### 500 - 

