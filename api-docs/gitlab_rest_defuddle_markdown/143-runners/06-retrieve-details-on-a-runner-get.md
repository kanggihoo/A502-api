# 06-Retrieve details on a runner [GET]

`GET /api/v4/runners/{id}`

Retrieves details of a runner. Instance runner details are available to all authenticated users through this endpoint. For groups and projects, you must have the Maintainer or Owner role for the associated project or group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of a runner |
| `include_projects` | `boolean` | `query` | No | Include projects in the response. Set to false to improve performance for runners with many projects. |

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
  "tag_list": string,
  "run_untagged": string,
  "locked": string,
  "maximum_timeout": string,
  "access_level": string,
  "version": string,
  "revision": string,
  "platform": string,
  "architecture": string,
  "contacted_at": string,
  "maintenance_note": string,
  "projects": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
    "default_branch": string,
    "tag_list": [
      string
    ],
    "topics": [
      string
    ],
    "ssh_url_to_repo": string,
    "http_url_to_repo": string,
    "web_url": string,
    "readme_url": string,
    "forks_count": integer,
    "license_url": string,
    "license": {
      "key": string,
      "name": string,
      "nickname": string,
      "html_url": string,
      "source_url": string,
    },
    "avatar_url": string,
    "star_count": integer,
    "last_activity_at": string,
    "visibility": string,
    "namespace": {
      "id": integer,
      "name": string,
      "path": string,
      "kind": string,
      "full_path": string,
      "parent_id": integer,
      "avatar_url": string,
      "web_url": string,
    },
    "custom_attributes": {
      "key": string,
      "value": string,
    },
    "repository_storage": string,
  },
  "groups": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - No access granted

#### 404 - Runner not found

