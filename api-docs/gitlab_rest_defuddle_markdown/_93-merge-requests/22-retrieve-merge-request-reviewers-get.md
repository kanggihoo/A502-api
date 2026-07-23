# 22-Retrieve merge request reviewers [GET]

`GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/reviewers`

Retrieves reviewers for a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "user": {
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
  },
  "state": string,
  "created_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not found

