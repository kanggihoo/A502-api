# 01-Get fields [GET]

`GET /rest/api/3/field`

Returns system and custom issue fields according to the following rules:

 *  Fields that cannot be added to the issue navigator are always returned.
 *  Fields that cannot be placed on an issue screen are always returned.
 *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches.
 *  Fields that are not associated to any used field configurations or screens are not returned.
 *  For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"clauseNames\":[\"description\"],\"custom\":false,\"id\":\"description\",\"name\":\"Description\",\"navigable\":true,\"orderable\":true,\"schema\":{\"system\":\"description\",\"type\":\"string\"},\"searchable\":true},{\"clauseNames\":[\"summary\"],\"custom\":false,\"id\":\"summary\",\"key\":\"summary\",\"name\":\"Summary\",\"navigable\":true,\"orderable\":true,\"schema\":{\"system\":\"summary\",\"type\":\"string\"},\"searchable\":true}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

