# 03-Get current usage of teams [GET]

`GET /api/v4/usage/teams`

Retrieve rounded total number of teams for this instance.
##### Permissions Must be authenticated.


### Responses

#### 200 - Total number of teams returned successfully

Schema (application/json):
```json
{
  "active": integer,
  "cloud_archived": integer,
  "teams": integer,
}
```

#### 401 - 

#### 500 - 

