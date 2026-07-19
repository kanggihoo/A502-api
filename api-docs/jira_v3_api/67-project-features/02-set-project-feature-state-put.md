# 02-Set project feature state [PUT]

`PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey}`

Sets the state of a project feature.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectIdOrKey` | `string` | `path` | Yes | The ID or (case-sensitive) key of the project. |
| `featureKey` | `string` | `path` | Yes | The key of the feature. |

### Request Body (application/json)

```json
{
  "state": enum("ENABLED" | "DISABLED" | "COMING_SOON"), // The feature state.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"features\":[{\"feature\":\"jsw.classic.roadmap\",\"imageUri\":\"https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-roadmap-feature.svg\",\"localisedDescription\":\"Your roadmap is an optimized location to create and manage your epics.\",\"localisedName\":\"Roadmap\",\"prerequisites\":[],\"projectId\":10001,\"state\":\"ENABLED\",\"toggleLocked\":true},{\"feature\":\"jsw.classic.backlog\",\"imageUri\":\"https://jira.atlassian.com/s/sb53l8/b/3/ab8a7691e4738b4f147e293f0864adfd5b8d3c85/_/download/resources/com.atlassian.jira.rest:classic-project-features/simple-backlog-feature.svg\",\"localisedDescription\":\"Plan and prioritize work in a dedicated space. To enable and configure the backlog for each board, go to board settings.\",\"localisedName\":\"Backlog\",\"prerequisites\":[],\"projectId\":10001,\"state\":\"ENABLED\",\"toggleLocked\":true}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

#### 404 - Returned if the project or project feature is not found.

