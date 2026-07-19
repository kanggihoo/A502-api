# 04-List all package pipelines [GET]

`GET /api/v4/projects/{id}/packages/{package_id}/pipelines`

Lists all pipelines for a specified package. The results are sorted by `id` in descending order. The results are paginated and return up to 20 records per page. This feature was introduced in GitLab 16.1.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `package_id` | `integer` | `path` | Yes | The ID of a package |
| `cursor` | `string` | `query` | No | Cursor for obtaining the next set of records |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
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
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

