# 12-Create an issue board [POST]

`POST /api/v4/projects/{id}/boards`

Creates an issue board in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string (required), // The board name
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "hide_backlog_list": boolean,
  "hide_closed_list": boolean,
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
  "lists": [
    {
      "id": integer,
      "label": {
        "id": integer,
        "name": string,
        "description": string,
        "text_color": string,
        "description_html": string,
        "color": string,
        "archived": boolean,
      },
      "position": integer,
      "milestone": {
        "id": integer,
        "iid": integer,
        "project_id": integer,
        "group_id": string,
        "title": string,
        "description": string,
        "state": string,
        "created_at": string,
        "updated_at": string,
        "due_date": string,
        "start_date": string,
        "expired": boolean,
        "web_url": string,
      },
      "iteration": {
        "id": integer,
        "iid": integer,
        "sequence": integer,
        "group_id": integer,
        "title": string,
        "description": string,
        "state": integer,
        "created_at": string,
        "updated_at": string,
        "start_date": string,
        "due_date": string,
        "web_url": string,
      },
      "assignee": {
        "id": integer,
        "username": string,
        "public_email": string,
        "name": string,
      },
      "max_issue_count": integer,
      "max_issue_weight": integer,
      "limit_metric": string,
    }
  ],
  "group": {
    "id": integer,
    "web_url": string,
    "name": string,
  },
  "milestone": {},
  "assignee": {
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
  "labels": {
    "id": integer,
    "name": string,
    "description": string,
    "text_color": string,
    "description_html": string,
    "color": string,
    "archived": boolean,
  },
  "weight": integer,
}
```

#### 400 - Bad Request

#### 404 - Not Found

