# 12-Retrieve a commit signature [GET]

`GET /api/v4/projects/{id}/repository/commits/{sha}/signature`

Retrieves the signature from a commit, if it is signed. For unsigned commits, it results in a 404 response.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `sha` | `string` | `path` | Yes | A commit sha, or the name of a branch or tag |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "signature_type": string,
  "signature": {},
  "commit_source": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

