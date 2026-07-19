# 12-Approve merge request [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approve`

Approves a specified merge request. The currently authenticated user must be an eligible approver. The `sha` parameter ensures you are approving the current version of the merge request. If defined, the value must match the merge request’s HEAD commit SHA. A mismatch returns a `409 Conflict` response.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "sha": string, // When present, must have the HEAD SHA of the source branch
  "publish_review": boolean, // When `true` submits pending review comments
  "approval_password": string, // Current user's password if project is set to require explicit auth on approval
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "user_has_approved": boolean,
  "user_can_approve": boolean,
  "approved": boolean,
  "approved_by": {
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
    "approved_at": string,
  },
}
```

#### 304 - Not modified

#### 400 - Bad Request

#### 401 - Unauthorized

#### 404 - Not found

