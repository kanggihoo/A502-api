# 02-Get reports [GET]

`GET /api/v4/compliance/reports`

Get a list of compliance reports previously created by page, selected with `page` and `per_page` query parameters.
##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of reports per page. |

### Responses

#### 200 - Compliance reports retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 501 - 

