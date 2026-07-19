# 07-NPM registry quick audit endpoint [POST]

`POST /api/v4/groups/{id}/-/packages/npm/-/npm/v1/security/audits/quick`

This feature was introduced in GitLab 15.6

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - Ok

#### 307 - Temporary Redirect

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

