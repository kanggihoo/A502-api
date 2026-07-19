# 38-Get latest public server release information [GET]

`GET /api/v4/latest_version`

Retrieves metadata about the latest Mattermost server release from GitHub.
##### Permissions Must have `manage_system` permission.


### Responses

#### 200 - Latest release metadata retrieval successful

Schema (application/json):
```json
{
  "id": integer,
  "tag_name": string,
  "name": string,
  "created_at": string,
  "published_at": string,
  "body": string,
  "html_url": string,
}
```

#### 401 - 

#### 403 - 

#### 500 - 

