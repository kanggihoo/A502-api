# 02-Create a freeze period [POST]

`POST /api/v4/projects/{id}/freeze_periods`

Creates a freeze period for a specified project. You must have the Maintainer or Owner role for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "freeze_start": string (required), // Start of the freeze period in cron format.
  "freeze_end": string (required), // End of the freeze period in cron format
  "cron_timezone": string, // The time zone for the cron fields, defaults to UTC if not provided
}
```
### Responses

#### 201 - Created

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

