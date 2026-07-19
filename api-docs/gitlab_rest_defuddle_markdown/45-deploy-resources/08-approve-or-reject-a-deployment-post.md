# 08-Approve or reject a deployment [POST]

`POST /api/v4/projects/{id}/deployments/{deployment_id}/approval`

Approves or rejects a deployment.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project owned by the authenticated user |
| `deployment_id` | `integer` | `path` | Yes | The ID of the deployment |

### Request Body (application/json)

```json
{
  "status": enum("approved" | "rejected") (required), // The status of the approval (either `approved` or `rejected`)
  "comment": string, // A comment to go with the approval
  "represented_as": string, // The name of the User/Group/Role to use for the approval, when the user belongs to multiple approval rules
}
```
### Responses

#### 201 - Created

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
  "status": string,
  "created_at": string,
  "comment": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

