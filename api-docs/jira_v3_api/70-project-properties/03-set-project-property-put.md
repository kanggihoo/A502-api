# 03-Set project property [PUT]

`PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}`

Sets the value of the [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties). You can use project properties to store custom data against the project.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the property is created.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The project ID or project key (case sensitive). |
| `propertyKey` | `string` | `path` | Yes | The key of the project property. The maximum length is 255 characters. |

### Request Body (application/json)

```json
any
```
### Responses

#### 200 - Returned if the project property is updated.

Schema (application/json):
```json
any
```

#### 201 - Returned if the project property is created.

Schema (application/json):
```json
any
```

#### 400 - Returned if the project key or id is invalid.

#### 401 - Returned if the authentication credentials are incorrect.

#### 403 - Returned if the user does not have permission to administer the project.

#### 404 - Returned if the project is not found.

