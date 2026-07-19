# 03-Search posts across all teams [POST]

`POST /api/v4/posts/search`

Search posts visible to the current user across all teams.
##### Permissions
Must be authenticated.


### Request Body (application/json)

```json
{
  "terms": string (required),
  "is_or_search": boolean,
  "time_zone_offset": integer,
  "include_deleted_channels": boolean,
  "page": integer,
  "per_page": integer,
}
```
### Responses

#### 200 - Post search successful

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

