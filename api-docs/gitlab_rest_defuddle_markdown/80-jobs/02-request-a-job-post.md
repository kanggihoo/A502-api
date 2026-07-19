# 02-Request a job [POST]

`POST /api/v4/jobs/request`

Request a job

### Request Body (application/json)

```json
{
  "token": string (required), // Runner's authentication token
  "system_id": string, // Runner's system identifier
  "last_update": string, // Runner's queue last_update token
  "info": {
    "name": string, // Runner's name
    "version": string, // Runner's version
    "revision": string, // Runner's revision
    "platform": string, // Runner's platform
    "architecture": string, // Runner's architecture
    "executor": string, // Runner's executor
    "features": {}, // Runner's features
    "config": {
      "gpus": string, // GPUs enabled
    }, // Runner's config
    "labels": {}, // Runner's labels
  }, // Runner's metadata
  "session": {
    "url": string, // Session's url
    "certificate": string, // Session's certificate
    "authorization": string, // Session's authorization
  }, // Runner's session data
}
```
### Responses

#### 201 - Job was scheduled

Schema (application/json):
```json
{
  "id": string,
  "token": string,
  "allow_git_fetch": string,
  "job_info": {
    "id": string,
    "name": string,
    "stage": string,
    "pipeline_id": string,
    "project_id": string,
    "project_name": string,
    "project_full_path": string,
    "namespace_id": string,
    "root_namespace_id": string,
    "organization_id": string,
    "instance_id": string,
    "instance_uuid": string,
    "user_id": string,
    "scoped_user_id": string,
    "time_in_queue_seconds": string,
    "project_jobs_running_on_instance_runners_count": string,
    "queue_size": string,
    "queue_depth": string,
  },
  "git_info": {
    "repo_url": string,
    "ref": string,
    "sha": string,
    "before_sha": string,
    "ref_type": string,
    "refspecs": string,
    "depth": string,
    "repo_object_format": string,
    "protected": string,
  },
  "runner_info": {
    "uuid": string,
    "timeout": string,
    "runner_session_url": string,
  },
  "inputs": string,
  "variables": string,
  "steps": {
    "name": string,
    "script": string,
    "timeout": string,
    "when": string,
    "allow_failure": string,
  },
  "hooks": {
    "name": string,
    "script": string,
  },
  "image": {
    "name": string,
    "entrypoint": string,
    "ports": {
      "number": string,
      "protocol": string,
      "name": string,
    },
    "executor_opts": string,
    "pull_policy": string,
  },
  "services": {
    "name": string,
    "entrypoint": string,
    "ports": {
      "number": string,
      "protocol": string,
      "name": string,
    },
    "executor_opts": string,
    "pull_policy": string,
    "alias": string,
    "command": string,
    "variables": string,
  },
  "artifacts": {
    "name": string,
    "untracked": string,
    "paths": string,
    "exclude": string,
    "when": string,
    "expire_in": string,
    "artifact_type": string,
    "artifact_format": string,
  },
  "cache": {
    "key": string,
    "untracked": string,
    "paths": string,
    "policy": string,
    "when": string,
    "fallback_keys": string,
  },
  "credentials": {
    "type": string,
    "url": string,
    "username": string,
    "password": string,
  },
  "features": string,
  "dependencies": string,
  "run": string,
  "suspend_options": string,
  "secrets": string,
  "policy_options": string,
}
```

#### 204 - No job for Runner

#### 400 - Bad Request

#### 403 - Forbidden

#### 409 - Conflict

#### 422 - Runner is orphaned

#### 429 - Too Many Requests

