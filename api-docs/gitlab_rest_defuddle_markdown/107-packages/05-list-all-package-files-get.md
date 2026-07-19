# 05-List all package files [GET]

`GET /api/v4/projects/{id}/packages/{package_id}/package_files`

Lists all package files for a specified package.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the project |
| `package_id` | `integer` | `path` | Yes | ID of a package |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `order_by` | `string` | `query` | No | Return package files ordered by `id`, `created_at` or `file_name` |
| `sort` | `string` | `query` | No | Return package files sorted in `asc` or `desc` order. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "package_id": integer,
  "created_at": string,
  "file_name": string,
  "size": integer,
  "file_md5": string,
  "file_sha1": string,
  "file_sha256": string,
  "pipelines": {
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
  },
}
```

#### 400 - Bad Request

#### 404 - Not Found

