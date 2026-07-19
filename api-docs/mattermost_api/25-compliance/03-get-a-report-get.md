# 03-Get a report [GET]

`GET /api/v4/compliance/reports/{report_id}`

Get a compliance reports previously created.
##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `report_id` | `string` | `path` | Yes | Compliance report GUID |

### Responses

#### 200 - Compliance report retrieval successful

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

