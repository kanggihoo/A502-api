# 10-Search teams [POST]

`POST /api/v4/teams/search`

Search teams based on search term and options provided in the request body.

##### Permissions
Logged in user only shows open teams
Logged in user with "manage_system" permission shows all teams


### Request Body (application/json)

```json
{
  "term": string, // The search term to match against the name or display name of teams
  "page": string, // The page number to return, if paginated. If this parameter is not present with the `per_page` parameter then the results will be returned un-paged.
  "per_page": string, // The number of entries to return per page, if paginated. If this parameter is not present with the `page` parameter then the results will be returned un-paged.
  "allow_open_invite": boolean, // Filters results to teams where `allow_open_invite` is set to true or false, excludes group constrained channels if this filter option is passed. If this filter option is not passed then the query will remain unchanged. __Minimum server version__: 5.28 
  "group_constrained": boolean, // Filters results to teams where `group_constrained` is set to true or false, returns the union of results when used with `allow_open_invite` If the filter option is not passed then the query will remain unchanged. __Minimum server version__: 5.28 
  "exclude_policy_constrained": boolean, // If set to true, only teams which do not have a granular retention policy assigned to them will be returned. The `sysconsole_read_compliance_data_retention` permission is required to use this parameter. __Minimum server version__: 5.35 
}
```
### Responses

#### 200 - Paginated teams response. (Note that the non-paginated response—returned if the request body does not contain both `page` and `per_page` fields—is a simple array of teams.)

Schema (application/json):
```json
{
  "teams": [
    {
      "id": string,
      "create_at": integer, // The time in milliseconds a team was created
      "update_at": integer, // The time in milliseconds a team was last updated
      "delete_at": integer, // The time in milliseconds a team was deleted
      "display_name": string,
      "name": string,
      "description": string,
      "email": string,
      "type": string,
      "allowed_domains": string,
      "invite_id": string,
      "allow_open_invite": boolean,
      "policy_id": string, // The data retention policy to which this team has been assigned. If no such policy exists, or the caller does not have the `sysconsole_read_compliance_data_retention` permission, this field will be null.
    }
  ], // The teams that matched the query.
  "total_count": number, // The total number of results, regardless of page and per_page requested.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

