# 15-Workhorse authorization for the reassignment CSV file [POST]

`POST /api/v4/groups/{id}/placeholder_reassignments/authorize`

Authorizes Workhorse to handle CSV file uploads for placeholder reassignments.
          This feature was introduced in GitLab 17.10

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

