# 03-List all to-do items [GET]

`GET /api/v4/todos`

Lists all to-do items. When no filter is applied, it returns all pending to-do items for the current user. Different filters allow the user to refine the request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `action` | `string` | `query` | No | The action to be filtered |
| `author_id` | `integer` | `query` | No | The ID of an author |
| `project_id` | `integer` | `query` | No | The ID of a project |
| `group_id` | `integer` | `query` | No | The ID of a group |
| `state` | `string` | `query` | No | The state of the to-do item |
| `type` | `string` | `query` | No | The type of to-do item |

### Responses

#### 200 - OK

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

