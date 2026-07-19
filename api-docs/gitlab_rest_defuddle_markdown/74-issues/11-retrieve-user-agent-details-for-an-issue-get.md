# 11-Retrieve user agent details for an issue [GET]

`GET /api/v4/projects/{id}/issues/{issue_iid}/user_agent_detail`

Retrieves user agent details for an issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `issue_iid` | `integer` | `path` | Yes | The internal ID of a project issue |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "user_agent": string,
  "ip_address": string,
  "akismet_submitted": boolean,
}
```

#### 400 - Bad Request

#### 404 - Not Found

