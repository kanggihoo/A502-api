# 01-Bulk get statuses [GET]

`GET /rest/api/3/statuses`

Returns a list of the statuses specified by one or more status IDs.

**[Permissions](#permissions) required:**

 *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
 *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `array` | `query` | Yes | The list of status IDs. To include multiple IDs, provide an ampersand-separated list. For example, id=10000&id=10001.<br><br>Min items `1`, Max items `50` |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"description\":\"The issue is resolved\",\"id\":\"1000\",\"name\":\"Finished\",\"scope\":{\"project\":{\"id\":\"1\"},\"type\":\"PROJECT\"},\"statusCategory\":\"DONE\"}]"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

