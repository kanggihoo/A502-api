# 05-Delete a freeze period [DEL]

`DELETE /api/v4/projects/{id}/freeze_periods/{freeze_period_id}`

Deletes a freeze period for a specified `freeze_period_id`. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `freeze_period_id` | `integer` | `path` | Yes | The ID of the freeze period |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "id": integer,
  "freeze_start": string,
  "freeze_end": string,
  "cron_timezone": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

