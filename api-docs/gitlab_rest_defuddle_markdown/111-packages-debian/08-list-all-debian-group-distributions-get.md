# 08-List all Debian group distributions [GET]

`GET /api/v4/groups/{id}/-/debian_distributions`

Lists all Debian distributions for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `codename` | `string` | `query` | No | The Debian Codename |
| `suite` | `string` | `query` | No | The Debian Suite |
| `origin` | `string` | `query` | No | The Debian Origin |
| `label` | `string` | `query` | No | The Debian Label |
| `version` | `string` | `query` | No | The Debian Version |
| `description` | `string` | `query` | No | The Debian Description |
| `valid_time_duration_seconds` | `integer` | `query` | No | The duration before the Release file should be considered expired by the client |
| `components` | `array` | `query` | No | The list of Components |
| `architectures` | `array` | `query` | No | The list of Architectures |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "codename": string,
  "suite": string,
  "origin": string,
  "label": string,
  "version": string,
  "description": string,
  "valid_time_duration_seconds": integer,
  "components": [
    string
  ],
  "architectures": [
    string
  ],
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

