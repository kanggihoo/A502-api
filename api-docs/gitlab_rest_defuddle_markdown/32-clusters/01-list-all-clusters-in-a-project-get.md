# 01-List all clusters in a project [GET]

`GET /api/v4/projects/{id}/clusters`

Lists all clusters in a specified project.

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
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not Found

