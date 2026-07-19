# 03-Get a single remote mirror [GET]

`GET /api/v4/projects/{id}/remote_mirrors/{mirror_id}`

Get a single remote mirror

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `mirror_id` | `string` | `path` | Yes | The ID of a remote mirror |

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

