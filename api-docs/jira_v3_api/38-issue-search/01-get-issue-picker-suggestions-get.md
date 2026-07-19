# 01-Get issue picker suggestions [GET]

`GET /rest/api/3/issue/picker`

Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string.

This operation returns two lists:

 *  `History Search` which includes issues from the user's history of created, edited, or viewed issues that contain the string in the `query` parameter.
 *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain the string in the `query` parameter.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `query` | `string` | `query` | No | A string to match against text fields in the issue such as title, description, or comments. |
| `currentJQL` | `string` | `query` | No | A JQL query defining a list of issues to search for the query term. Note that `username` and `userkey` cannot be used as search terms for this parameter, due to privacy reasons. Use `accountId` instead. |
| `currentIssueKey` | `string` | `query` | No | The key of an issue to exclude from search results. For example, the issue the user is viewing when they perform this query. |
| `currentProjectId` | `string` | `query` | No | The ID of a project that suggested issues must belong to. |
| `showSubTasks` | `boolean` | `query` | No | Indicate whether to include subtasks in the suggestions list. |
| `showSubTaskParent` | `boolean` | `query` | No | When `currentIssueKey` is a subtask, whether to include the parent issue in the suggestions if it matches the query. |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "sections": [
    {
      "id": string, // The ID of the type of issues suggested for use in auto-completion.
      "issues": [
        {
          "id": integer, // The ID of the issue.
          "img": string, // The URL of the issue type's avatar.
          "key": string, // The key of the issue.
          "keyHtml": string, // The key of the issue in HTML format.
          "summary": string, // The phrase containing the query string in HTML format, with the string highlighted with HTML bold tags.
          "summaryText": string, // The phrase containing the query string, as plain text.
        }
      ], // A list of issues suggested for use in auto-completion.
      "label": string, // The label of the type of issues suggested for use in auto-completion.
      "msg": string, // If no issue suggestions are found, returns a message indicating no suggestions were found,
      "sub": string, // If issue suggestions are found, returns a message indicating the number of issues suggestions found and returned.
    }
  ], // A list of issues for an issue type suggested for use in auto-completion.
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

