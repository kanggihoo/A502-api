# 01-Bulk get custom field configurations [POST]

`POST /rest/api/3/app/field/context/configuration/list`

Returns a [paginated](#pagination) list of configurations for list of custom fields of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).

The result can be filtered by one of these criteria:

 *  `id`.
 *  `fieldContextId`.
 *  `issueId`.
 *  `projectKeyOrId` and `issueTypeId`.

Otherwise, all configurations for the provided list of custom fields are returned.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that provided the custom field type.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `array` | `query` | No | The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`. |
| `fieldContextId` | `array` | `query` | No | The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: `fieldContextId=10000&fieldContextId=10001`. Can't be provided with `id`, `issueId`, `projectKeyOrId`, or `issueTypeId`. |
| `issueId` | `integer` | `query` | No | The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with `projectKeyOrId`, or `issueTypeId`. |
| `projectKeyOrId` | `string` | `query` | No | The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`. |
| `issueTypeId` | `string` | `query` | No | The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Request Body (application/json)

```json
{
  "fieldIdsOrKeys": [
    string
  ] (required), // List of IDs or keys of the custom fields. It can be a mix of IDs and keys in the same query.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"isLast\":true,\"maxResults\":1000,\"startAt\":0,\"total\":2,\"values\":[{\"customFieldId\":\"customfield_10035\",\"fieldContextId\":\"10010\",\"id\":\"10000\"},{\"configuration\":{\"maxValue\":10000,\"minValue\":0},\"customFieldId\":\"customfield_10036\",\"fieldContextId\":\"10011\",\"id\":\"10001\",\"schema\":{\"properties\":{\"amount\":{\"type\":\"number\"},\"currency\":{\"type\":\"string\"}},\"required\":[\"amount\",\"currency\"]}}]}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user is not a Jira admin or the request is not authenticated as from the app that provided the field.

#### 404 - Returned if the custom field is not found.

