# 04-Deletes a custom project template [DELETE]

`DELETE /rest/api/3/project-template/remove-template`

Remove custom template

This API endpoint allows you to remove a specified customised template

***Note: Custom Templates are only supported for Jira Enterprise edition.***

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `templateKey` | `string` | `query` | Yes | The \{@link String\} containing the key of the custom template to remove |

### Responses

#### 200 - 200 response

Schema (application/json):
```json
any
```

