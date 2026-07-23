# 01-Search project code using natural language [GET]

`GET /api/v4/projects/{id}/(-/)search/semantic`

Introduced in GitLab 18.11.

Searches indexed project code using semantic (meaning-based) similarity rather than
keyword matching. Use this when you do not know the exact symbol or file name, or
to discover how a behavior is implemented across the codebase.

Primary use cases:
- When you do not know the exact symbol or file path
- To see how a behavior or feature is implemented across the codebase
- To discover related implementations (clients, jobs, workers)

How to use:
- Provide a concise, specific query with concrete keywords
- Use directory_path to narrow scope (e.g. "app/services/")
- Prefer precise intent over broad terms

Results are grouped by file. Each file includes merged line ranges with content
and a relevance score (0.0-1.0). The response includes an overall confidence
level (high/medium/low/unknown) based on score distribution. Results are
filtered by Duo context exclusion settings.

Requires semantic code search to be enabled and indexed for the project namespace.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `q` | `string` | `query` | Yes | Natural language search query (e.g. "authentication middleware", "rate limiting logic") |
| `directory_path` | `string` | `query` | No | Restrict search to files under this directory path (e.g. "app/services/"). Must be a relative path — no leading slash, no .. segments. |
| `knn` | `integer` | `query` | No | Number of nearest neighbours to retrieve internally (default: 64). Higher values improve recall at the cost of latency. |
| `limit` | `integer` | `query` | No | Maximum number of results to return (default: 20). |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "confidence": string,
  "results": [
    {
      "path": string,
      "blob_id": string,
      "file_url": string,
      "score": number,
      "snippet_ranges": [
        {
          "start_line": integer,
          "end_line": integer,
          "content": string,
          "score": number,
        }
      ],
    }
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found - project not found or semantic code search unavailable

#### 422 - Unprocessable entity - project has no embeddings

#### 429 - Too many requests

