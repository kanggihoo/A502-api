# 33-Trigger a test webhook [POST]

`POST /api/v4/projects/{id}/hooks/{hook_id}/test/{trigger}`

Triggers a test webhook. This endpoint has a rate limit of five requests per minute for each webhook and authenticated user. To disable this limit on GitLab Self-Managed and GitLab Dedicated, an administrator can disable the feature flag named web_hook_test_api_endpoint_rate_limit.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |
| `trigger` | `string` | `path` | Yes | The type of trigger hook |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 201 - Created

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

#### 429 - Too many requests

