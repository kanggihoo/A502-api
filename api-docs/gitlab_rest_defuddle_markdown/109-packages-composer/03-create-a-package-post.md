# 03-Create a package [POST]

`POST /api/v4/projects/{id}/packages/composer`

Creates a Composer package from a specified Git tag or branch for a project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of a project |

### Request Body (application/json)

```json
{
  "branch": string, // The name of the branch
  "tag": string, // The name of the tag
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

