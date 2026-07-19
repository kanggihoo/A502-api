# 03-Remove modules [DELETE]

`DELETE /rest/atlassian-connect/1/app/module/dynamic`

Remove all or a list of modules registered by the calling app.

**[Permissions](#permissions) required:** Only Connect apps can make this request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `moduleKey` | `array` | `query` | No | The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter.<br>For example, `moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field`.<br>Nonexistent keys are ignored. |

### Responses

#### 204 - Returned if the request is successful.

#### 401 - Returned if the call is not from a Connect app.

Example (application/json):
```json
{
  "message": "The request is not from a Connect app."
}
```

