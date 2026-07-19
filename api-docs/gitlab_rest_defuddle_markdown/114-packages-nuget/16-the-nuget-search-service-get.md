# 16-The NuGet Search Service [GET]

`GET /api/v4/groups/{id}/-/packages/nuget/query`

This feature was introduced in GitLab 12.8

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The group ID or full group path. |
| `q` | `string` | `query` | No | The search term |
| `skip` | `integer` | `query` | No | The number of results to skip |
| `take` | `integer` | `query` | No | The number of results to return |
| `prerelease` | `boolean` | `query` | No | Include prerelease versions |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "totalHits": integer,
  "data": [
    {
      "@type": string,
      "id": string,
      "title": string,
      "totalDownloads": integer,
      "verified": boolean,
      "version": string,
      "versions": {
        "@id": string,
        "version": string,
        "downloads": integer,
      },
      "tags": string,
      "authors": string,
      "description": string,
      "summary": string,
      "projectUrl": string,
      "licenseUrl": string,
      "iconUrl": string,
    }
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

