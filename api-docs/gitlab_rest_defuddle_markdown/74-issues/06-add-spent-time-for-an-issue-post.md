# 06-Add spent time for an issue [POST]

`POST /api/v4/projects/{id}/issues/{issue_iid}/add_spent_time`

Adds spent time for a specified issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of the issue. |

### Request Body (application/json)

```json
{
  "duration": string (required), // The duration in human format.
}
```
### Responses

#### 201 - Created

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

