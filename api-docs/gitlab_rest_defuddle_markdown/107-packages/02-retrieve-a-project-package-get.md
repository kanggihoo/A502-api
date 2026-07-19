# 02-Retrieve a project package [GET]

`GET /api/v4/projects/{id}/packages/{package_id}`

Retrieves a specified project package. Only packages with status `default` or `deprecated` are returned.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `package_id` | `integer` | `path` | Yes | The ID of a package |

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

#### 404 - Not Found

