# 01-Apply a suggestion to a merge request [PUT]

`PUT /api/v4/suggestions/{id}/apply`

Applies a suggested patch in a merge request. You must have the Developer, Maintainer, or Owner role.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the suggestion |

### Request Body (application/json)

```json
{
  "commit_message": string, // A custom commit message to use instead of the default generated message or the project's default message
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "from_line": integer,
  "to_line": integer,
  "appliable": boolean,
  "applied": boolean,
  "from_content": string,
  "to_content": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

