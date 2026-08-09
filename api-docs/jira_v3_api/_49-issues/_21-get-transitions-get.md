# 21-Get transitions [GET]

`GET /rest/api/3/issue/{issueIdOrKey}/transitions`

Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status.

Note, if a request is made for a transition that does not exist or cannot be performed on the issue, given its status, the response will return any empty transitions list.

This operation can be accessed anonymously.

**[Permissions](#permissions) required: A list or transition is returned only when the user has:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

However, if the user does not have the *Transition issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information about transitions in the response. This parameter accepts `transitions.fields`, which returns information about the fields in the transition screen for each transition. Fields hidden from the screen are not returned. Use this information to populate the `fields` and `update` fields in [Transition issue](#api-rest-api-3-issue-issueIdOrKey-transitions-post). |
| `transitionId` | `string` | `query` | No | The ID of the transition. |
| `skipRemoteOnlyCondition` | `boolean` | `query` | No | Whether transitions with the condition *Hide From User Condition* are included in the response. Available to Connect and Forge app users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). |
| `includeUnavailableTransitions` | `boolean` | `query` | No | Whether details of transitions that fail a condition are included in the response |
| `sortByOpsBarAndStatus` | `boolean` | `query` | No | Whether the transitions are sorted by ops-bar sequence value first then category order (Todo, In Progress, Done) or only by ops-bar sequence value. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"transitions\":[{\"fields\":{\"summary\":{\"allowedValues\":[\"red\",\"blue\"],\"defaultValue\":\"red\",\"hasDefaultValue\":false,\"key\":\"field_key\",\"name\":\"My Multi Select\",\"operations\":[\"set\",\"add\"],\"required\":false,\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiselect\",\"customId\":10001,\"items\":\"option\",\"type\":\"array\"}}},\"hasScreen\":false,\"id\":\"2\",\"isAvailable\":true,\"isConditional\":false,\"isGlobal\":false,\"isInitial\":false,\"name\":\"Close Issue\",\"to\":{\"description\":\"The issue is currently being worked on.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/progress.gif\",\"id\":\"10000\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/10000\",\"statusCategory\":{\"colorName\":\"yellow\",\"id\":1,\"key\":\"in-flight\",\"name\":\"In Progress\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/1\"}}},{\"fields\":{\"summary\":{\"allowedValues\":[\"red\",\"blue\"],\"defaultValue\":\"red\",\"hasDefaultValue\":false,\"key\":\"field_key\",\"name\":\"My Multi Select\",\"operations\":[\"set\",\"add\"],\"required\":false,\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiselect\",\"customId\":10001,\"items\":\"option\",\"type\":\"array\"}},\"colour\":{\"allowedValues\":[\"red\",\"blue\"],\"defaultValue\":\"red\",\"hasDefaultValue\":false,\"key\":\"field_key\",\"name\":\"My Multi Select\",\"operations\":[\"set\",\"add\"],\"required\":false,\"schema\":{\"custom\":\"com.atlassian.jira.plugin.system.customfieldtypes:multiselect\",\"customId\":10001,\"items\":\"option\",\"type\":\"array\"}}},\"hasScreen\":true,\"id\":\"711\",\"name\":\"QA Review\",\"to\":{\"description\":\"The issue is closed.\",\"iconUrl\":\"https://your-domain.atlassian.net/images/icons/closed.gif\",\"id\":\"5\",\"name\":\"Closed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/status/5\",\"statusCategory\":{\"colorName\":\"green\",\"id\":9,\"key\":\"completed\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/statuscategory/9\"}}}]}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue is not found or the user does not have permission to view it.

