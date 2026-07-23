# 06-Search all private and open type channels across all teams [POST]

`POST /api/v4/channels/search`

Returns all private and open type channels where 'term' matches on the name, display name, or purpose of
the channel.

Configured 'default' channels (ex Town Square and Off-Topic) can be excluded from the results
with the `exclude_default_channels` boolean parameter.

Channels that are associated (via GroupChannel records) to a given group can be excluded from the results
with the `not_associated_to_group` parameter and a group id string.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `system_console` | `boolean` | `query` | No | Is the request from system_console. If this is set to true, it filters channels by the logged in user.<br> |

### Request Body (application/json)

```json
{
  "term": string (required), // The string to search in the channel name, display name, and purpose.
  "not_associated_to_group": string, // A group id to exclude channels that are associated to that group via GroupChannel records.
  "exclude_default_channels": boolean, // Exclude default channels from the results by setting this parameter to true.
  "team_ids": [
    string
  ], // Filters results to channels belonging to the given team ids  __Minimum server version__: 5.26 
  "group_constrained": boolean, // Filters results to only return channels constrained to a group  __Minimum server version__: 5.26 
  "exclude_group_constrained": boolean, // Filters results to exclude channels constrained to a group  __Minimum server version__: 5.26 
  "public": boolean, // Filters results to only return Public / Open channels, can be used in conjunction with `private` to return both `public` and `private` channels  __Minimum server version__: 5.26 
  "private": boolean, // Filters results to only return Private channels, can be used in conjunction with `public` to return both `private` and `public` channels  __Minimum server version__: 5.26 
  "deleted": boolean, // Filters results to only return deleted / archived channels  __Minimum server version__: 5.26 
  "page": string, // The page number to return, if paginated. If this parameter is not present with the `per_page` parameter then the results will be returned un-paged.
  "per_page": string, // The number of entries to return per page, if paginated. If this parameter is not present with the `page` parameter then the results will be returned un-paged.
  "exclude_policy_constrained": boolean, // If set to true, only channels which do not have a granular retention policy assigned to them will be returned. The `sysconsole_read_compliance_data_retention` permission is required to use this parameter. __Minimum server version__: 5.35 
  "include_search_by_id": boolean, // If set to true, returns channels where given search 'term' matches channel ID. __Minimum server version__: 5.35 
  "exclude_remote": boolean, // If set to true, only returns channels that are local to this server. __Minimum server version__: 10.2 
}
```
### Responses

#### 200 - Paginated channel response. (Note that the non-paginated response—returned if the request body does not contain both `page` and `per_page` fields—is a simple array of channels.)

Schema (application/json):
```json
{
  "channels": [
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
  ], // The channels that matched the query.
  "total_count": number, // The total number of results, regardless of page and per_page requested.
}
```

#### 400 - 

#### 401 - 

