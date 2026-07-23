# 113-Trigger a slash command for mattermost-slash-commands [POST]

`POST /api/v4/projects/{id}/integrations/mattermost_slash_commands/trigger`

Added in GitLab 8.13

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "token": string (required), // The Mattermost token.
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

