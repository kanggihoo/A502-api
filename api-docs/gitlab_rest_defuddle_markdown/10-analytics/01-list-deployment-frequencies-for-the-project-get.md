# 01-List deployment frequencies for the project [GET]

`GET /api/v4/projects/{id}/analytics/deployment_frequency`

List deployment frequencies for the project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `environment` | `string` | `query` | Yes | Name of the environment to filter by |
| `from` | `string` | `query` | Yes | Datetime to start from, inclusive |
| `to` | `string` | `query` | No | Datetime to end at, exclusive |
| `interval` | `string` | `query` | No | Interval to roll-up data by |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "value": string,
  "from": string,
  "to": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

