# 21-Create a test run [POST]

`POST /api/v4/hooks/{hook_id}`

Creates a test run for a webhook. Executes the webhook with mock data.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not Found

