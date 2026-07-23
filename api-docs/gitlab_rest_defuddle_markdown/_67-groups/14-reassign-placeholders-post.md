# 14-Reassign placeholders [POST]

`POST /api/v4/groups/{id}/placeholder_reassignments`

Reassigns placeholder users with an uploaded CSV file.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // The CSV file containing the reassignments
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

