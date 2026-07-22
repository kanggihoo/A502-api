# 06-Retrieve count of recently created merge requests for a group [GET]

`GET /api/v4/analytics/group_activity/merge_requests_count`

Retrieves the count of recently created merge requests for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_path` | `string` | `query` | Yes | Group path |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "merge_requests_count": integer, // Number of merge requests. Limited to 1000
}
```

#### 400 - Bad Request

