# 01-Create report [POST]

`POST /api/v4/compliance/reports`

Create and save a compliance report.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 201 - Compliance report creation successful

Schema (application/json):
```json
{
  "id": string,
  "create_at": integer,
  "user_id": string,
  "status": string,
  "count": integer,
  "desc": string,
  "type": string,
  "start_at": integer,
  "end_at": integer,
  "keywords": string,
  "emails": string,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

