# 01-The NuGet V3 Feed Service Index [GET]

`GET /api/v4/projects/{id}/packages/nuget/index`

This feature was introduced in GitLab 12.6

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "version": string,
  "resources": [
    {}
  ],
}
```

#### 400 - Bad Request

#### 404 - Not Found

