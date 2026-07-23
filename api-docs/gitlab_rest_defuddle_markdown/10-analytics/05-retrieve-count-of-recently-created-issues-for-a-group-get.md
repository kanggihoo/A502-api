# 05-Retrieve count of recently created issues for a group [GET]

`GET /api/v4/analytics/group_activity/issues_count`

Retrieves the count of recently created issues for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_path` | `string` | `query` | Yes | Group path |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "issues_count": integer, // Number of issues. Limited to 1000
}
```

#### 400 - Bad Request

