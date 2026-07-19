# 01-Publish a new component project release as version to the CI/CD catalog [POST]

`POST /api/v4/projects/{id}/catalog/publish`

Publishes a release of a catalog resource as version to the CI/CD catalog.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "metadata": {} (required), // The metadata for the release
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "catalog_url": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

