# 01-List all group variables [GET]

`GET /api/v4/groups/{id}/variables`

Lists all variables for a specified group. Use the `page` and `per_page` pagination parameters to control the pagination of results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a group or URL-encoded path of the group owned by the authenticated<br>      user |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "variable_type": string,
  "key": string,
  "value": string,
  "hidden": boolean,
  "protected": boolean,
  "masked": boolean,
  "raw": boolean,
  "environment_scope": string,
  "description": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

