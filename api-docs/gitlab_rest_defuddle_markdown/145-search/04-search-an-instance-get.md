# 04-Search an instance [GET]

`GET /api/v4/search`

Searches for a term across the entire GitLab instance. The response depends on the requested scope.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | `string` | `query` | Yes | The expression it should be searched for |
| `scope` | `string` | `query` | Yes | The scope of the search |
| `state` | `string` | `query` | No | Filter results by state |
| `confidential` | `boolean` | `query` | No | Filter results by confidentiality |
| `type` | `array` | `query` | No | Filter work items by type. Only applies to work_items scope. Available types: issue, task, epic, incident, test_case, requirement, objective, key_result, ticket. |
| `include_archived` | `boolean` | `query` | No | Includes archived projects in the search. Introduced in GitLab 18.9. |
| `fields` | `array` | `query` | No | Array of fields you wish to search. Available with advanced search. |
| `exclude_forks` | `boolean` | `query` | No | Excludes forked projects in the search. Available with exact code search. Introduced in GitLab 18.9. |
| `num_context_lines` | `integer` | `query` | No | Number of context lines around each match. Available with advanced and exact code search. Introduced in GitLab 18.11. |
| `regex` | `boolean` | `query` | No | Performs a regex code search. Available with exact code search. Introduced in GitLab 18.9 |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

#### 400 - Bad Request

