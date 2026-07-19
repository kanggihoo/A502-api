# 01-Create a to-do item for an issuable [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/todo`

Creates a to-do item for the current user on a specified issuable. If a to-do item already exists for the user on that issuable, returns a `304` status code.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `merge_request_iid` | `integer` | `path` | Yes | The internal ID of an issuable |

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "project": {
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
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
  "author": {
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
  "action_name": string,
  "target_type": string,
  "target": {},
  "target_url": string,
  "body": string,
  "state": string,
  "created_at": string,
  "updated_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

