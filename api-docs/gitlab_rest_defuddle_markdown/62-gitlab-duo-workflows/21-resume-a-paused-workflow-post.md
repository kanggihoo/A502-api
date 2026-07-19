# 21-Resume a paused workflow [POST]

`POST /api/v4/ai/duo_workflows/workflows/{workflow_id}/resume`

Resume a paused workflow

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `workflow_id` | `string` | `path` | Yes | The ID of the workflow to resume |

### Request Body (application/json)

```json
{
  "human_approval": boolean (required), // Whether the human approves resuming the workflow
  "human_message": string, // Optional message accompanying the human decision
}
```
### Responses

#### 201 - Created

#### 400 - Validation failed

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

