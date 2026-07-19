# 11-Delete a Debian group distribution [DEL]

`DELETE /api/v4/groups/{id}/-/debian_distributions/{codename}`

Deletes a specified Debian group distribution for a group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `codename` | `string` | `path` | Yes | The Debian Codename |
| `suite` | `string` | `query` | No | The Debian Suite |
| `origin` | `string` | `query` | No | The Debian Origin |
| `label` | `string` | `query` | No | The Debian Label |
| `version` | `string` | `query` | No | The Debian Version |
| `description` | `string` | `query` | No | The Debian Description |
| `valid_time_duration_seconds` | `integer` | `query` | No | The duration before the Release file should be considered expired by the client |
| `components` | `array` | `query` | No | The list of Components |
| `architectures` | `array` | `query` | No | The list of Architectures |

### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not Found

