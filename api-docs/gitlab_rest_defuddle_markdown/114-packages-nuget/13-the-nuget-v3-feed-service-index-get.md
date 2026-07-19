# 13-The NuGet V3 Feed Service Index [GET]

`GET /api/v4/groups/{id}/-/packages/nuget/index`

This feature was introduced in GitLab 12.6

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The group ID or full group path. |

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

