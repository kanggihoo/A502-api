# 01-Start the pull mirroring process for a project [POST]

`POST /api/v4/projects/{id}/mirror/pull`

Starts the pull mirroring process for a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "action": string, // Pull Request action
  "pull_request.number": integer, // Pull request IID
  "pull_request.head.ref": string, // Source branch
  "pull_request.head.sha": string, // Source sha
  "pull_request.head.repo.full_name": string, // Source repository
  "pull_request.base.ref": string, // Target branch
  "pull_request.base.sha": string, // Target sha
  "pull_request.base.repo.full_name": string, // Target repository
}
```
### Responses

#### 200 - OK

#### 400 - The project is not mirrored

#### 403 - Mirroring for the project is on pause

#### 404 - Not Found

#### 422 - The pull request event is not processable

