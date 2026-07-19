# 12-Resend a webhook event [POST]

`POST /api/v4/groups/{id}/hooks/{hook_id}/events/{hook_log_id}/resend`

Resends a webhook event. This endpoint has a rate limit of five requests per minute for each webhook and authenticated user. To disable this limit on GitLab Self-Managed and GitLab Dedicated, an administrator can disable the feature flag named web_hook_event_resend_api_endpoint_rate_limit.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `hook_id` | `integer` | `path` | Yes | The ID of a group hook |
| `hook_log_id` | `any` | `path` | Yes |  |

### Responses

#### 201 - Created

#### 400 - Bad Request

#### 404 - Not found

#### 422 - Unprocessable entity

#### 429 - Too many requests

