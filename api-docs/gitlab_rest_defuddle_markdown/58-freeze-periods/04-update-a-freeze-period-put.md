# 04-Update a freeze period [PUT]

`PUT /api/v4/projects/{id}/freeze_periods/{freeze_period_id}`

Updates a freeze period for a specified `freeze_period_id`. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `freeze_period_id` | `integer` | `path` | Yes | The ID of the freeze period |

### Request Body (application/json)

```json
{
  "freeze_start": string, // Start of the freeze period in cron format
  "freeze_end": string, // End of the freeze period in cron format
  "cron_timezone": string, // The time zone for the cron fields
}
```
### Responses

#### 200 - OK

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

