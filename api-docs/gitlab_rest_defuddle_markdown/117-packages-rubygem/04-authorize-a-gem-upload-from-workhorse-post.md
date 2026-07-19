# 04-Authorize a gem upload from workhorse [POST]

`POST /api/v4/projects/{id}/packages/rubygems/api/v1/gems/authorize`

This feature was introduced in GitLab 13.9

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

