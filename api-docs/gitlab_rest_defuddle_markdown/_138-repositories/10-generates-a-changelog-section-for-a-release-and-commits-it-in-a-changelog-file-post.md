# 10-Generates a changelog section for a release and commits it in a changelog file [POST]

`POST /api/v4/projects/{id}/repository/changelog`

This feature was introduced in GitLab 13.9

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "from": string, // The first commit in the range of commits to use for the changelog
  "to": string, // The last commit in the range of commits to use for the changelog
  "date": string, // The date and time of the release
  "trailer": string, // The Git trailer to use for determining if commits are to be included in the changelog
  "config_file": string, // The file path to the configuration file as stored in the project's Git repository. Defaults to '.gitlab/changelog_config.yml'
  "config_file_ref": string, // The git reference (for example, branch) where the changelog configuration file is defined. Defaults to the default repository branch.
  "branch": string, // The branch to commit the changelog changes to
  "file": string, // The file to commit the changelog changes to
  "message": string, // The commit message to use when committing the changelog
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

