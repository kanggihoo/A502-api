# 06-Search on GitLab within a project [GET]

`GET /api/v4/projects/{id}/(-/)search`

This feature was introduced in GitLab 10.5.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `search` | `string` | `query` | Yes | The expression it should be searched for |
| `scope` | `string` | `query` | Yes | The scope of the search |
| `ref` | `string` | `query` | No | The name of a repository branch or tag. If not given, the default branch is used |
| `state` | `string` | `query` | No | Filter results by state |
| `confidential` | `boolean` | `query` | No | Filter results by confidentiality |
| `type` | `array` | `query` | No | Filter work items by type. Only applies to work_items scope. Available types: issue, task, epic, incident, test_case, requirement, objective, key_result, ticket. |
| `fields` | `array` | `query` | No | Array of fields you wish to search. Available with advanced search. |
| `num_context_lines` | `integer` | `query` | No | Number of context lines around each match. Available with advanced and exact code search. Introduced in GitLab 18.11. |
| `regex` | `boolean` | `query` | No | Performs a regex code search. Available with exact code search. Introduced in GitLab 18.9 |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

