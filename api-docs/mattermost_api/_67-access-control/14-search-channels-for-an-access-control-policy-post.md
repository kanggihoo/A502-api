# 14-Search channels for an access control policy [POST]

`POST /api/v4/access_control_policies/{policy_id}/resources/channels/search`

Searches for channels associated with a specific access control policy based on search criteria.
##### Permissions
Must have the `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `policy_id` | `string` | `path` | Yes | The ID of the access control policy. |

### Request Body (application/json)

```json
{
  "term": string, // The string to search in the channel name, display name, and purpose.
  "team_ids": [
    string
  ], // Filters results to channels belonging to the given team ids.
  "public": boolean, // Filters results to only return Public / Open channels.
  "private": boolean, // Filters results to only return Private channels.
  "deleted": boolean, // Filters results to only return deleted / archived channels.
  "include_deleted": boolean, // Whether to include deleted channels in the search results.
}
```
### Responses

#### 200 - Channel search results retrieved successfully.

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

