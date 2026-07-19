# 03-Delete a GitLab for Jira (Forge) namespace subscription [DEL]

`DELETE /api/v4/integrations/jira_forge/subscriptions/{id}`

Unsubscribes a GitLab namespace from the Forge installation.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the subscription to delete |

### Responses

#### 204 - No Content

Schema (application/json):
```json
{
  "success": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

