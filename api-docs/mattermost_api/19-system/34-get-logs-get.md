# 34-Get logs [GET]

`GET /api/v4/logs`

Get a page of server logs, selected with `page` and `logs_per_page` query parameters.
##### Permissions
Must have `manage_system` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `logs_per_page` | `string` | `query` | No | The number of logs per page. There is a maximum limit of 10000 logs per page. |

### Responses

#### 200 - Logs retrieval successful

Schema (application/json):
```json
[
  string
]
```

#### 403 - 

