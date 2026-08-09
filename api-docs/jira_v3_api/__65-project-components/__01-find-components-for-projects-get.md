# 01-Find components for projects [GET]

`GET /rest/api/3/component`

Returns a [paginated](#pagination) list of all components in a project, including global (Compass) components when applicable.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdsOrKeys` | `array` | `query` | No | The project IDs and/or project keys (case sensitive). |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |
| `orderBy` | `string` | `query` | No | [Order](#ordering) the results by a field:<br><br> *  `description` Sorts by the component description.<br> *  `name` Sorts by component name. |
| `query` | `string` | `query` | No | Filter the results using a literal string. Components with a matching `name` or `description` are returned (case insensitive). |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":false,\"maxResults\":2,\"startAt\":0,\"total\":2,\"values\":[{\"description\":\"This is a component\",\"id\":\"10000\",\"name\":\"Component1\",\"self\":\"http://www.example.com/jira/rest/api/2/component/10000\"},{\"ari\":\"ari:cloud:graph::integration-context/ecda99d9-9b42-4bf7-8b4f-ecb5fcf5868c/component/10001\",\"description\":\"This is a global component\",\"id\":\"10001\",\"metadata\":{\"key1\":\"value1\",\"key2\":\"value2\"},\"name\":\"Component2\",\"self\":\"http://www.example.com/jira/rest/api/2/component/10001\"}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have permission to view it.

