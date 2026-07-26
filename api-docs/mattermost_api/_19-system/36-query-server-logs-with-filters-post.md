# 36-Query server logs with filters [POST]

`POST /api/v4/logs/query`

Query server logs using filter criteria.
##### Permissions Must have `get_logs` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | The page to select. |
| `logs_per_page` | `string` | `query` | No | The number of logs per page. |

### Request Body (application/json)

```json
{
  "server_names": [
    string
  ],
  "log_levels": [
    string
  ],
  "date_from": string, // Inclusive start of the time range. The server parses this using the layout `YYYY-MM-DD HH:MM:SS.mmm ±HH:MM` (milliseconds optional; timezone offset required), matching Go reference time `2006-01-02 15:04:05.999 -07:00`. 
  "date_to": string, // Inclusive end of the time range. Same format as `date_from` (`YYYY-MM-DD HH:MM:SS.mmm ±HH:MM`, e.g. `2006-01-02 15:04:05.999 -07:00`). 
}
```
### Responses

#### 200 - Log query successful

Schema (application/json):
```json
{}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

