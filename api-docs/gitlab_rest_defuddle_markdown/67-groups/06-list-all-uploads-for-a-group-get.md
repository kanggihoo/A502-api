# 06-List all uploads for a group [GET]

`GET /api/v4/groups/{id}/uploads`

Lists all uploads for a specified group sorted by `created_at` in descending order. You must have the Maintainer or Owner role for the group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "size": integer,
  "filename": string,
  "created_at": string,
  "uploaded_by": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
  },
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

