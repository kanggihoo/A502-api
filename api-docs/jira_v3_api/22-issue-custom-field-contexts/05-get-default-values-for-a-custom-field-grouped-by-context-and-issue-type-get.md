# 05-Get default values for a custom field grouped by context and issue type [GET]

`GET /rest/api/3/field/{fieldId}/context/defaultValues`

Returns a paginated list of default values grouped by custom field context.

Each returned \{@code ContextDefaultValuesBean\} has a \{@code contextId\} and a \{@code defaultValues\} list of \{@code IssueTypeDefaultValueBean\} entries \\u2014 one per issue-type-scoped default value configured for the context. An entry with \{@code "isAnyIssueType": true\} represents the catch-all default that applies to every issue type covered by the context that is not covered by a more specific entry; a non-null \{@code issueTypeId\} represents a default that only applies to that issue type.

For contexts that have not been converted to the multiple-contexts data model, exactly one entry is returned per context with \{@code isAnyIssueType=true\}. For converted contexts, one entry is returned per configured per-issue-type default.

The value object on each entry is the same polymorphic \{@code CustomFieldContextDefaultValueBean\} exposed by the deprecated \{@code GET /defaultValue\} endpoint \\u2014 its concrete subtype depends on the custom field's type (see the list of supported types on that endpoint).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldId` | `string` | `path` | Yes | The ID of the custom field, for example `customfield\_10000`. |
| `contextId` | `array` | `query` | No | The IDs of the contexts to return default values for. If omitted, default values for every context the custom field has are returned. |
| `issueTypeId` | `array` | `query` | No | The IDs of the issue types to restrict the returned per-issue-type default values to. If omitted, default values for every issue type are returned. This filter never removes the catch-all \{@code isAnyIssueType\} entry of a context. |
| `startAt` | `integer` | `query` | No | The index of the first item to return in a page of results (page offset). |
| `maxResults` | `integer` | `query` | No | The maximum number of items to return per page. |

### Responses

#### 200 - Returned if the request is successful.

Schema (application/json):
```json
{
  "isLast": boolean, // Whether this is the last page.
  "maxResults": integer, // The maximum number of items that could be returned.
  "nextPage": string, // If there is another page of results, the URL of the next page.
  "self": string, // The URL of the page.
  "startAt": integer, // The index of the first item returned.
  "total": integer, // The number of items returned.
  "values": [
    {
      "contextId": integer (required), // The ID of the context.
      "defaultValues": [
        {
          "isAnyIssueType": boolean, // True when this default value applies to every issue type covered by the context (no specific issue type). Only present when true; omitted otherwise.
          "issueTypeId": string, // The ID of the issue type this default value applies to. Null when isAnyIssueType is true.
          "value": {},
        }
      ], // Per-issue-type default values for this context. May contain a single entry for unconverted contexts, or one entry per issue type for converted contexts.
    }
  ], // The list of items.
}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the required permissions.

Example (application/json):
```json
"{\"errorMessages\":[\"Only Jira administrators can access custom field contexts.\"],\"errors\":{}}"
```

#### 404 - Returned if the custom field is not found.

Example (application/json):
```json
"{\"errorMessages\":[\"The custom field was not found.\"],\"errors\":{}}"
```

