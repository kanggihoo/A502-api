# 05-List all GitLab CI/CD YAML templates [GET]

`GET /api/v4/templates/gitlab_ci_ymls`

Lists all GitLab CI/CD YAML templates.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "name": string,
}
```

#### 400 - Bad Request

