# 01-Retrieve namespace subscription [GET]

`GET /api/v4/namespaces/{id}/gitlab_subscription`

Retrieves GitLab subscription details for a specified namespace.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "plan": {},
  "usage": {},
  "billing": {},
}
```

#### 404 - Not Found

