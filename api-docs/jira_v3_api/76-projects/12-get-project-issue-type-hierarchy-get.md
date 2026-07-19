# 12-Get project issue type hierarchy [GET]

`GET /rest/api/3/project/{projectId}/hierarchy`

Get the issue type hierarchy for a next-gen project.

The issue type hierarchy for a project consists of:

 *  *Epic* at level 1 (optional).
 *  One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic.
 *  *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `integer` | `path` | Yes | The ID of the project. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"hierarchy\":[{\"issueTypes\":[{\"avatarId\":10324,\"entityId\":\"ce32639b-8911-4689-81da-65681f451516\",\"id\":10008,\"name\":\"Story\"},{\"avatarId\":10324,\"entityId\":\"ffdbced5-fbfc-4370-a848-94e2ce3751af\",\"id\":10001,\"name\":\"Bug\"}],\"level\":0,\"name\":\"Base\"},{\"issueTypes\":[{\"avatarId\":10179,\"entityId\":\"80f20d47-34dc-4680-8937-936b7e762a35\",\"id\":10007,\"name\":\"Epic\"}],\"level\":1,\"name\":\"Epic\"},{\"issueTypes\":[{\"avatarId\":10573,\"entityId\":\"210b4879-15cc-414c-9746-f8f6b6be0a72\",\"id\":10009,\"name\":\"Subtask\"}],\"level\":-1,\"name\":\"Subtask\"}],\"projectId\":10030}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the project is not found or the user does not have the necessary permission.

