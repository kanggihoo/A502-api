# 05-List all runners [GET]

`GET /api/v4/runners/all`

Lists all runners in the GitLab instance (project and shared). You must have either administrator access or auditor access.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `scope` | `string` | `query` | No | Deprecated: Use `type` or `status` instead. The scope of runners to return |
| `type` | `string` | `query` | No | The type of runners to return |
| `paused` | `boolean` | `query` | No | Whether to include only runners that are accepting or ignoring new jobs |
| `status` | `string` | `query` | No | The status of runners to return |
| `tag_list` | `array` | `query` | No | A list of runner tags |
| `version_prefix` | `string` | `query` | No | The version prefix of runners to return |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "ip_address": string,
  "active": boolean,
  "paused": boolean,
  "is_shared": boolean,
  "runner_type": string,
  "name": string,
  "online": boolean,
  "created_by": {
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
  "created_at": string,
  "status": string,
  "job_execution_status": string,
}
```

#### 400 - Scope contains invalid value

#### 401 - Unauthorized

