# 25-Get managed category mappings [GET]

`GET /api/v4/teams/{team_id}/channels/managed_categories`

Returns a map of channel ID to managed category name for all channels the requesting user is a member of in the given team that have a managed category assigned.

Requires an Enterprise license and the `ManagedChannelCategories` feature flag to be enabled.

##### Permissions
Must be authenticated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team ID |

### Responses

#### 200 - Managed category mappings retrieved successfully

Schema (application/json):
```json
{}
```

#### 401 - 

#### 404 - Returned when the `ManagedChannelCategories` feature flag is disabled.

#### 501 - Returned when the server does not have an Enterprise license.

