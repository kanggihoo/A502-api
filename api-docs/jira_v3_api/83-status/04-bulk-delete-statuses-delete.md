# 04-Bulk delete Statuses [DELETE]

`DELETE /rest/api/3/statuses`

Deletes statuses by ID.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `array` | `query` | Yes | The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.<br><br>Min items `1`, Max items `50` |

### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid.

Example (application/json):
```json
"{\"errorMessages\":[\"The name is too long, maxSize=255\"],\"errors\":{}}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

