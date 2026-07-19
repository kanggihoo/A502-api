# 09-Delete a runner controller [DEL]

`DELETE /api/v4/runner_controllers/{id}`

Deletes a specified runner controller. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the runner controller |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

