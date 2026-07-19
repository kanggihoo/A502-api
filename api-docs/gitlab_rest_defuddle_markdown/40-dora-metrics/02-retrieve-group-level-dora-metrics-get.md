# 02-Retrieve group-level DORA metrics [GET]

`GET /api/v4/groups/{id}/dora/metrics`

Retrieves DORA metrics for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the group |
| `metric` | `string` | `query` | Yes | One of `deployment_frequency`, `lead_time_for_changes`, `time_to_restore_service` or `change_failure_rate` |
| `start_date` | `string` | `query` | No | Date range to start from. ISO 8601 Date format, for example `2021-03-01`. Default is 3 months ago |
| `end_date` | `string` | `query` | No | Date range to end at. ISO 8601 Date format, for example `2021-03-01`. Default is the current date |
| `interval` | `string` | `query` | No | The bucketing interval. One of `all`, `monthly` or `daily`. Default is `daily` |
| `environment_tiers` | `array` | `query` | No | The tiers of the environments. Default is `production` |

### Responses

#### 200 - successful operation

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

