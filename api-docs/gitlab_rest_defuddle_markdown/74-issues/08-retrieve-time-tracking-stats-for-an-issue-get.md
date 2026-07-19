# 08-Retrieve time tracking stats for an issue [GET]

`GET /api/v4/projects/{id}/issues/{issue_iid}/time_stats`

Retrieves time tracking stats for a specified issue, including time estimate and time spent in seconds and human-readable format (for example, `1h 30m`).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of the issue |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "time_estimate": integer,
  "total_time_spent": integer,
  "human_time_estimate": string,
  "human_total_time_spent": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

