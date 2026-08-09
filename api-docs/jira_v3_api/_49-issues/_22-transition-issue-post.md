# 22-Transition issue [POST]

`POST /rest/api/3/issue/{issueIdOrKey}/transitions`

Performs an issue transition and, if the transition has a screen, updates the fields from the transition screen.

sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Transition issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `issueIdOrKey` | `string` | `path` | Yes | The ID or key of the issue. |

### Request Body (application/json)

```json
{
  "fields": {}, // List of issue screen fields to update, specifying the sub-field to update and its value for each field. This field provides a straightforward option when setting a sub-field. When multiple sub-fields or other operations are required, use `update`. Fields included in here cannot be included in `update`.
  "historyMetadata": any, // Additional issue history details.
  "properties": [
    {
      "key": string, // The key of the property. Required on create and update.
      "value": any, // The value of the property. Required on create and update.
    }
  ], // Details of issue properties to be add or update.
  "transition": any, // Details of a transition. Required when performing a transition, optional when creating or editing an issue.
  "update": {}, // A Map containing the field field name and a list of operations to perform on the issue screen field. Note that fields included in here cannot be included in `fields`.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if:

 *  no transition is specified.
 *  the user does not have permission to transition the issue.
 *  a field that isn't included on the transition screen is defined in `fields` or `update`.
 *  a field is specified in both `fields` and `update`.
 *  the request is invalid for any other reason.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 404 - Returned if the issue is not found or the user does not have permission to view it.

#### 409 - Returned if the issue could not be updated due to a conflicting update.

#### 413 - Returned if a per-issue limit has been breached for one of the following fields:

 *  comments
 *  worklogs
 *  attachments
 *  issue links
 *  remote issue links

#### 422 - Returned if a configuration problem prevents the creation of the issue.

