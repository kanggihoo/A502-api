# 16-Search for team posts [POST]

`POST /api/v4/teams/{team_id}/posts/search`

Search posts in the team and from the provided terms string.
##### Permissions
Must be authenticated and have the `view_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (application/json)

```json
{
  "terms": string (required), // The search terms as inputed by the user. To search for posts from a user include `from:someusername`, using a user's username. To search in a specific channel include `in:somechannel`, using the channel name (not the display name).
  "is_or_search": boolean (required), // Set to true if an Or search should be performed vs an And search.
  "time_zone_offset": integer, // Offset from UTC of user timezone for date searches.
  "include_deleted_channels": boolean, // Set to true if deleted channels should be included in the search. (archived channels)
  "page": integer, // The page to select. (Only works with Elasticsearch)
  "per_page": integer, // The number of posts per page. (Only works with Elasticsearch)
}
```
### Responses

#### 200 - Post list retrieval successful

Schema (application/json):
```json
{
  "order": [
    string
  ],
  "posts": {},
  "matches": {}, // A mapping of post IDs to a list of matched terms within the post. This field will only be populated on servers running version 5.1 or greater with Elasticsearch enabled.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

