# 19-Returns the list of pipeline refs for the project [GET]

`GET /api/v4/geo/repositories/{gl_repository}/pipeline_refs`

Returns the list of pipeline refs for the project

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `gl_repository` | `string` | `path` | Yes | The repository to check |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "pipeline_refs": [
    string
  ],
}
```

#### 400 - Bad Request

#### 401 - 401 Unauthorized

#### 404 - 404 Not found

