# 01-List all pipeline schedules [GET]

`GET /api/v4/projects/{id}/pipeline_schedules`

Lists all pipeline schedules for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `scope` | `string` | `query` | No | The scope of pipeline schedules |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "ref": string,
  "cron": string,
  "cron_timezone": string,
  "next_run_at": string,
  "active": boolean,
  "created_at": string,
  "updated_at": string,
  "owner": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "inputs": {
    "name": string,
    "value": string,
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

