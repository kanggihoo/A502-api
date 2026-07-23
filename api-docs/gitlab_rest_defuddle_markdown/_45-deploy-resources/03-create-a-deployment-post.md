# 03-Create a deployment [POST]

`POST /api/v4/projects/{id}/deployments`

Creates a deployment.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |

### Request Body (application/json)

```json
{
  "environment": string (required), // The name of the environment to create the deployment for
  "sha": string (required), // The SHA of the commit that is deployed
  "ref": string (required), // The name of the branch or tag that is deployed
  "tag": boolean (required), // A boolean that indicates if the deployed ref is a tag (`true`) or not (`false`)
  "status": enum("running" | "success" | "failed" | "canceled") (required), // The status of the deployment that is created. One of `running`, `success`, `failed`, or `canceled`
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
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
  "pending_approval_count": integer,
  "approvals": {
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
    "status": string,
    "created_at": string,
    "comment": string,
  },
  "approval_summary": {
    "rules": {
      "id": integer,
      "user_id": integer,
      "group_id": integer,
      "access_level": integer,
      "access_level_description": string,
      "required_approvals": integer,
      "group_inheritance_type": integer,
      "deployment_approvals": {
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
        "status": string,
        "created_at": string,
        "comment": string,
      },
    },
  },
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

