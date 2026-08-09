# 05-Bulk get statuses by name [GET]

`GET /rest/api/3/statuses/byNames`

Returns a list of the statuses specified by one or more status names.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Browse projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `array` | `query` | Yes | The list of status names. To include multiple names, provide an ampersand-separated list. For example, name=nameXX&name=nameYY.<br><br>Min items `1`, Max items `50` |
| `projectId` | `string` | `query` | No | The project the status is part of or null for global statuses. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"The issue is resolved\",\"id\":\"1000\",\"name\":\"Finished\",\"scope\":{\"project\":{\"id\":\"1\"},\"type\":\"PROJECT\"},\"statusCategory\":\"DONE\"}]"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

