# 01-List all packages for a project [GET]

`GET /api/v4/projects/{id}/packages`

Lists all packages for a specified project. All package types are included in results. Unauthenticated requests return only packages of public projects. By default, packages with `default`, `deprecated`, and `error` status are returned. Use the `status` parameter to view other packages.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `order_by` | `string` | `query` | No | Return packages ordered by `created_at`, `name`, `version` or `type` fields. |
| `sort` | `string` | `query` | No | Return packages sorted in `asc` or `desc` order. |
| `package_type` | `string` | `query` | No | Return packages of a certain type |
| `package_name` | `string` | `query` | No | Return packages with this name |
| `package_version` | `string` | `query` | No | Return packages with this version |
| `include_versionless` | `boolean` | `query` | No | Returns packages without a version |
| `status` | `string` | `query` | No | Return packages with specified status |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "conan_package_name": string,
  "version": string,
  "package_type": string,
  "status": string,
  "_links": string,
  "created_at": string,
  "last_downloaded_at": string,
  "creator_id": integer, // ID of the user who created the package
  "project_id": integer,
  "project_path": string,
  "tags": string,
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
  "versions": {
    "id": string,
    "version": string,
    "created_at": string,
    "tags": string,
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
  },
}
```

#### 400 - Bad Request

#### 403 - Forbidden

#### 404 - Project Not Found

