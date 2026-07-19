# 02-Authorize package upload from workhorse [POST]

`POST /api/v4/projects/{id}/packages/rpm/authorize`

This feature was introduced in GitLab 15.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

