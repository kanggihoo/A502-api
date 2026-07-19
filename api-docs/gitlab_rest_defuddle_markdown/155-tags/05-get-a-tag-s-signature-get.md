# 05-Get a tag's signature [GET]

`GET /api/v4/projects/{id}/repository/tags/{tag_name}/signature`

Get a tag's signature

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `tag_name` | `string` | `path` | Yes | The name of the tag |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "signature_type": string,
  "signature": {},
}
```

#### 400 - Bad Request

#### 404 - Not found

