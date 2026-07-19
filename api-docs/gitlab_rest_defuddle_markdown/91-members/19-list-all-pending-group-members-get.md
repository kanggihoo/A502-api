# 19-List all pending group members [GET]

`GET /api/v4/groups/{id}/pending_members`

Lists all members in an `awaiting` state and those who are invited but do not have a GitLab account for a specified group and any subgroups and projects. This operation works on top-level groups only. It does not work on subgroups.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

#### 400 - Bad Request

#### 404 - Not Found

