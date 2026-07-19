# 02-Create remote mirror for a project [POST]

`POST /api/v4/projects/{id}/remote_mirrors`

Create remote mirror for a project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "url": string (required), // The URL for a remote mirror
  "enabled": boolean, // Determines if the mirror is enabled
  "auth_method": enum("ssh_public_key" | "password"), // Determines the mirror authentication method
  "keep_divergent_refs": boolean, // Determines if divergent refs are kept on the target
  "only_protected_branches": boolean, // Determines if only protected branches are mirrored
  "mirror_branch_regex": string, // Determines if only matched branches are mirrored
  "host_keys": [
    string
  ], // SSH host keys in bare format (ssh-ed25519 AAAA...) or full known_hosts format (hostname ssh-ed25519 AAAA...). Bare keys use the hostname from the mirror URL.
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

