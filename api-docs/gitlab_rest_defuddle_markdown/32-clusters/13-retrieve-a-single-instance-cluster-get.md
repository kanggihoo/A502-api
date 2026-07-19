# 13-Retrieve a single instance cluster [GET]

`GET /api/v4/admin/clusters/{cluster_id}`

Retrieves a specified instance cluster.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Not found

