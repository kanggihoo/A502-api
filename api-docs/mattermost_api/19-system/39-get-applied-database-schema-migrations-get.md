# 39-Get applied database schema migrations [GET]

`GET /api/v4/system/schema/version`

Returns the list of applied database schema migrations.
##### Permissions Must have at least one sysconsole read permission.


### Responses

#### 200 - Applied schema migrations retrieval successful

Schema (application/json):
```json
[
  {
    "version": integer,
    "name": string,
  }
]
```

#### 401 - 

#### 403 - 

#### 500 - 

