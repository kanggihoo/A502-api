# 10-List all participants in an issue [GET]

`GET /api/v4/projects/{id}/issues/{issue_iid}/participants`

Lists all users that are participants in a specified issue. If the project is private or the issue is confidential, you need to provide credentials to authorize. In most cases, you should authenticate with a personal access token.

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
  "id": integer,
  "username": string,
  "public_email": string,
  "name": string,
  "state": string,
  "locked": boolean,
  "avatar_url": string,
  "avatar_path": string,
  "custom_attributes": [
    {
      "key": string,
      "value": string,
    }
  ],
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

