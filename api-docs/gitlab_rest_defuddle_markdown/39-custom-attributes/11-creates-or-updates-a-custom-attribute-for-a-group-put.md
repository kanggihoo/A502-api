# 11-Creates or updates a custom attribute for a group [PUT]

`PUT /api/v4/groups/{id}/custom_attributes/{key}`

Creates or updates a custom attribute for a specified group. If the attribute already exists, it is updated, otherwise a new attribute is created.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `key` | `string` | `path` | Yes | The key of the custom attribute |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "value": string (required), // The value of the custom attribute
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "key": string,
  "value": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

