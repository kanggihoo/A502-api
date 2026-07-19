# 05-Add a cluster to a project [POST]

`POST /api/v4/projects/{id}/clusters/user`

Adds a cluster to a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // Cluster name
  "enabled": boolean, // Determines if cluster is active or not, defaults to true
  "domain": string, // Cluster base domain
  "environment_scope": string, // The associated environment to the cluster
  "namespace_per_environment": boolean, // Deploy each environment to a separate Kubernetes namespace
  "management_project_id": integer, // The ID of the management project
  "managed": boolean, // Determines if GitLab will manage namespaces and service accounts for this cluster, defaults to true
  "platform_kubernetes_attributes": {
    "api_url": string (required), // URL to access the Kubernetes API
    "token": string (required), // Token to authenticate against Kubernetes
    "ca_cert": string, // TLS certificate (needed if API is using a self-signed TLS certificate)
    "namespace": string, // Unique namespace related to Project
    "authorization_type": enum("unknown_authorization" | "rbac" | "abac"), // Cluster authorization type, defaults to RBAC
  } (required), // Platform Kubernetes data
}
```
### Responses

#### 201 - Created

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

#### 400 - Validation error

#### 403 - Forbidden

#### 404 - Not found

