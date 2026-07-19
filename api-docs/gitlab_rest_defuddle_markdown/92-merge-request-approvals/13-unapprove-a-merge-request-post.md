# 13-Unapprove a merge request [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/unapprove`

Unapproves a merge request. Removes the approval for the currently authenticated user from a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

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

