# 02-Retrieve a cluster from a project [GET]

`GET /api/v4/projects/{id}/clusters/{cluster_id}`

Retrieves a specified cluster in a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `cluster_id` | `integer` | `path` | Yes | The cluster ID |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "name": string,
  "created_at": string,
  "domain": string,
  "enabled": string,
  "managed": string,
  "provider_type": string,
  "platform_type": string,
  "environment_scope": string,
  "cluster_type": string,
  "namespace_per_environment": string,
  "user": {
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
  "platform_kubernetes": {
    "api_url": string,
    "namespace": string,
    "authorization_type": string,
    "ca_cert": string,
  },
  "provider_gcp": {
    "cluster_id": string,
    "status_name": string,
    "gcp_project_id": string,
    "zone": string,
    "machine_type": string,
    "num_nodes": string,
    "endpoint": string,
  },
  "management_project": {
    "id": integer,
    "description": string,
    "name": string,
    "name_with_namespace": string,
    "path": string,
    "path_with_namespace": string,
    "created_at": string,
  },
  "project": {
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
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

