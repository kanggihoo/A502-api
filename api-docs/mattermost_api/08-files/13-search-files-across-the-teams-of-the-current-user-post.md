# 13-Search files across the teams of the current user [POST]

`POST /api/v4/files/search`

Search for files in the teams of the current user based on file name, extention and file content (if file content extraction is enabled and supported for the files).
__Minimum server version__: 10.2
##### Permissions
Must be authenticated and have the `view_team` permission.


### Request Body (multipart/form-data)

```json
{
  "terms": string (required), // The search terms as entered by the user. To search for files from a user include `from:someusername`, using a user's username. To search in a specific channel include `in:somechannel`, using the channel name (not the display name). To search for specific extensions include `ext:extension`.
  "is_or_search": boolean (required), // Set to true if an Or search should be performed vs an And search.
  "time_zone_offset": integer, // Offset from UTC of user timezone for date searches.
  "include_deleted_channels": boolean, // Set to true if deleted channels should be included in the search. (archived channels)
  "page": integer, // The page to select. (Only works with Elasticsearch)
  "per_page": integer, // The number of posts per page. (Only works with Elasticsearch)
}
```
### Responses

#### 200 - Files list retrieval successful

Schema (application/json):
```json
{
  "order": [
    string
  ],
  "file_infos": {},
  "next_file_id": string, // The ID of next file info. Not omitted when empty or not relevant.
  "prev_file_id": string, // The ID of previous file info. Not omitted when empty or not relevant.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

