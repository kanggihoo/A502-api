# 09-Generates a changelog section for a release and returns it [GET]

`GET /api/v4/projects/{id}/repository/changelog`

This feature was introduced in GitLab 14.6

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `version` | `string` | `query` | Yes | The version of the release, using the semantic versioning format |
| `from` | `string` | `query` | No | The first commit in the range of commits to use for the changelog |
| `to` | `string` | `query` | No | The last commit in the range of commits to use for the changelog |
| `date` | `string` | `query` | No | The date and time of the release |
| `trailer` | `string` | `query` | No | The Git trailer to use for determining if commits are to be included in the changelog |
| `config_file` | `string` | `query` | No | The file path to the configuration file as stored in the project's Git repository. Defaults to '.gitlab/changelog_config.yml' |
| `config_file_ref` | `string` | `query` | No | The git reference (for example, branch) where the changelog configuration file is defined. Defaults to the default repository branch. |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "notes": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

