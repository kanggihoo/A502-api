# 32-List all events [GET]

`GET /api/v4/projects/{id}/hooks/{hook_id}/events`

Lists all events for a specified webhook.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `status` | `array` | `query` | No | HTTP status code of the event |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `page` | `integer` | `query` | No | Current page number |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `hook_id` | `integer` | `path` | Yes | The ID of the hook |

### Responses

#### 200 - OK

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not found

