# 01-List the project's remote mirrors [GET]

`GET /api/v4/projects/{id}/remote_mirrors`

List the project's remote mirrors

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "enabled": boolean,
  "url": string,
  "update_status": string,
  "last_update_at": string,
  "last_update_started_at": string,
  "last_successful_update_at": string,
  "last_error": string,
  "only_protected_branches": boolean,
  "keep_divergent_refs": boolean,
  "auth_method": string,
  "host_keys": [
    {
      "fingerprint_sha256": string,
    }
  ],
  "mirror_branch_regex": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

