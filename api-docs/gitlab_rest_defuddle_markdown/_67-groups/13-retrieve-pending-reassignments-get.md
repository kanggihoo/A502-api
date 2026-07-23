# 13-Retrieve pending reassignments [GET]

`GET /api/v4/groups/{id}/placeholder_reassignments`

Retrieves a CSV file with a list of pending reassignments. This feature was introduced in GitLab 17.10.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

