# 27-Retrieve association counts for a user [GET]

`GET /api/v4/users/{id}/associations_count`

Retrieves the number of groups, projects, issues, and merge requests associated with a specified user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the user to query. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "groups_count": string,
  "projects_count": string,
  "issues_count": string,
  "merge_requests_count": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

