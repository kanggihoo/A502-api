# 02-Get project property [GET]

`GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}`

Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `propertyKey` | `string` | `path` | Yes | The project property key. Use [Get project property keys](#api-rest-api-3-project-projectIdOrKey-properties-get) to get a list of all project property keys. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"key\":\"issue.support\",\"value\":{\"system.conversation.id\":\"b1bf38be-5e94-4b40-a3b8-9278735ee1e6\",\"system.support.time\":\"1m\"}}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - Returned if the user does not have permission to view the project.

#### 404 - Returned if the project or property is not found.

