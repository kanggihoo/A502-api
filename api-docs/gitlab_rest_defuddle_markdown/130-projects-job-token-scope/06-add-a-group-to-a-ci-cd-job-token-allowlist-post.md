# 06-Add a group to a CI/CD job token allowlist [POST]

`POST /api/v4/projects/{id}/job_token_scope/groups_allowlist`

Adds a group to the CI/CD job token allowlist of a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of user project |

### Request Body (application/json)

```json
{
  "target_group_id": integer (required), // ID of target group
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "web_url": string,
  "name": string,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

