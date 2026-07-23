# 05-Retrieve an environment [GET]

`GET /api/v4/projects/{id}/environments/{environment_id}`

Retrieves a specified environment for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `environment_id` | `integer` | `path` | Yes | The ID of the environment |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "slug": string,
  "external_url": string,
  "created_at": string,
  "updated_at": string,
  "tier": string,
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
  "last_deployment": {
    "id": integer,
    "iid": integer,
    "ref": string,
    "sha": string,
    "created_at": string,
    "updated_at": string,
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
    "environment": {
      "id": integer,
      "name": string,
      "slug": string,
      "external_url": string,
      "created_at": string,
      "updated_at": string,
    },
    "deployable": {
      "id": integer,
      "status": string,
      "stage": string,
      "name": string,
      "ref": string,
      "tag": boolean,
      "coverage": number,
      "allow_failure": boolean,
      "created_at": string,
      "started_at": string,
      "finished_at": string,
      "erased_at": string,
      "duration": number, // Time spent running
      "queued_duration": number, // Time spent enqueued
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
        "created_at": string,
        "bio": string,
        "location": string,
        "linkedin": string,
        "twitter": string,
        "discord": string,
        "website_url": string,
        "github": string,
        "job_title": string,
        "pronouns": string,
        "organization": string,
        "bot": boolean,
        "work_information": string,
        "followers": string,
        "following": string,
        "is_followed": string,
        "local_time": string,
      },
      "commit": {
        "id": string,
        "short_id": string,
        "created_at": string,
        "parent_ids": [
          string
        ],
        "title": string,
        "message": string,
        "author_name": string,
        "author_email": string,
        "authored_date": string,
        "committer_name": string,
        "committer_email": string,
        "committed_date": string,
        "trailers": {},
        "extended_trailers": {},
        "web_url": string,
      },
      "pipeline": {
        "id": integer,
        "iid": integer,
        "project_id": integer,
        "sha": string,
        "ref": string,
        "status": string,
        "source": string,
        "created_at": string,
        "updated_at": string,
        "web_url": string,
      },
      "failure_reason": string,
      "web_url": string,
      "project": string,
      "artifacts_file": {
        "filename": string,
        "size": integer,
      },
      "artifacts": [
        {
          "file_type": string,
          "size": integer,
          "filename": string,
          "file_format": string,
        }
      ],
      "runner": {
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
      },
      "runner_manager": {
        "id": integer,
        "system_id": string,
        "version": string,
        "revision": string,
        "platform": string,
        "architecture": string,
        "created_at": string,
        "contacted_at": string,
        "ip_address": string,
        "status": string,
        "job_execution_status": string,
      },
      "artifacts_expire_at": string,
      "archived": boolean,
      "tag_list": [
        string
      ],
    },
    "status": string,
  },
  "state": string,
  "auto_stop_at": string,
  "cluster_agent": {
    "id": integer,
    "name": string,
    "config_project": {
      "id": integer,
      "description": string,
      "name": string,
      "name_with_namespace": string,
      "path": string,
      "path_with_namespace": string,
      "created_at": string,
    },
    "created_at": string,
    "created_by_user_id": integer,
    "is_receptive": boolean,
  },
  "kubernetes_namespace": string,
  "flux_resource_path": string,
  "description": string,
  "auto_stop_setting": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

