# 09-List all custom attributes for a group [GET]

`GET /api/v4/groups/{id}/custom_attributes`

Lists all custom attributes for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "value": string,
}
```

#### 404 - Not Found

