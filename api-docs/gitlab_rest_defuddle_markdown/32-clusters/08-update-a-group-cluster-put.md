# 08-Update a group cluster [PUT]

`PUT /api/v4/groups/{id}/clusters/{cluster_id}`

Updates a specified group cluster.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of the group |
| `cluster_id` | `integer` | `path` | Yes | The cluster ID |

### Request Body (application/json)

```json
{
  "name": string, // Cluster name
  "enabled": boolean, // Determines if cluster is active or not
  "domain": string, // Cluster base domain
  "environment_scope": string, // The associated environment to the cluster
  "namespace_per_environment": boolean, // Deploy each environment to a separate Kubernetes namespace
  "management_project_id": integer, // The ID of the management project
  "managed": boolean, // Determines if GitLab will manage namespaces and service accounts for this cluster
  "platform_kubernetes_attributes": {
    "api_url": string, // URL to access the Kubernetes API
    "token": string, // Token to authenticate against Kubernetes
    "ca_cert": string, // TLS certificate (needed if API is using a self-signed TLS certificate)
    "namespace": string, // Unique namespace related to Group
  }, // Platform Kubernetes data
}
```
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
  "group": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
}
```

#### 400 - Validation error

#### 403 - Forbidden

#### 404 - Not found

