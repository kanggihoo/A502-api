# 05-Retrieve details of a registry repository tag [GET]

`GET /api/v4/projects/{id}/registry/repositories/{repository_id}/tags/{tag_name}`

Retrieves details of a specified registry repository tag.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `repository_id` | `integer` | `path` | Yes | The ID of the repository |
| `tag_name` | `string` | `path` | Yes | The name of the tag |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "name": string,
  "path": string,
  "location": string,
  "revision": string,
  "short_revision": string,
  "digest": string,
  "created_at": string,
  "total_size": integer,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not Found

