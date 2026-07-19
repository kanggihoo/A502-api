# 01-Get audit records [GET]

`GET /rest/api/3/auditing/record`

Returns a list of audit records. The list can be filtered to include items:

 *  where each item in `filter` has at least one match in any of these fields:
    
     *  `summary`
     *  `category`
     *  `eventSource`
     *  `objectItem.name` If the object is a user, account ID is available to filter.
     *  `objectItem.parentName`
     *  `objectItem.typeName`
     *  `changedValues.changedFrom`
     *  `changedValues.changedTo`
     *  `remoteAddress`
    
    For example, if `filter` contains *man ed*, an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned.
 *  created on or after a date and time.
 *  created or or before a date and time.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `offset` | `integer` | `query` | No | The number of records to skip before returning the first result. |
| `limit` | `integer` | `query` | No | The maximum number of results to return. |
| `filter` | `string` | `query` | No | The strings to match with audit field content, space separated. |
| `from` | `string` | `query` | No | The date and time on or after which returned audit records must have been created. If `to` is provided `from` must be before `to` or no audit records are returned. |
| `to` | `string` | `query` | No | The date and time on or before which returned audit results must have been created. If `from` is provided `to` must be after `from` or no audit records are returned. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"limit\":1000,\"offset\":0,\"records\":[{\"associatedItems\":[{\"id\":\"jira-software-users\",\"name\":\"jira-software-users\",\"parentId\":\"1\",\"parentName\":\"Jira Internal Directory\",\"typeName\":\"GROUP\"}],\"authorAccountId\":\"5ab8f18d741e9c2c7e9d4538\",\"authorKey\":\"administrator\",\"category\":\"user management\",\"changedValues\":[{\"changedFrom\":\"user@atlassian.com\",\"changedTo\":\"newuser@atlassian.com\",\"fieldName\":\"email\"}],\"created\":\"2014-03-19T18:45:42.967+0000\",\"description\":\"Optional description\",\"eventSource\":\"Jira Connect Plugin\",\"id\":1,\"objectItem\":{\"id\":\"user\",\"name\":\"user\",\"parentId\":\"1\",\"parentName\":\"Jira Internal Directory\",\"typeName\":\"USER\"},\"remoteAddress\":\"192.168.1.1\",\"summary\":\"User created\"}],\"total\":1}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

#### 403 - Returned if:

 *  the user does not have the required permissions.
 *  all Jira products are on free plans. Audit logs are available when at least one Jira product is on a paid plan.

Schema (application/json):
```json
{
  "errorMessages": [
    string
  ], // The list of error messages produced by this operation. For example, "input parameter 'key' must be provided"
  "errors": {}, // The list of errors by parameter returned by the operation. For example,"projectKey": "Project keys must start with an uppercase letter, followed by one or more uppercase alphanumeric characters."
  "status": integer,
}
```

