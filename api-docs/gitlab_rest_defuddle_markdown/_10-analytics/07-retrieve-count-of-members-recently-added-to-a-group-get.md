# 07-Retrieve count of members recently added to a group [GET]

`GET /api/v4/analytics/group_activity/new_members_count`

Retrieves the count of members recently added to a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `group_path` | `string` | `query` | Yes | Group path |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "new_members_count": integer, // Number of new members. Limited to 1000
}
```

#### 400 - Bad Request

