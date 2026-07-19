# 13-Search field scheme fields [GET]

`GET /rest/api/3/config/fieldschemes/{id}/fields`

Search for fields belonging to a given field association scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `startAt` | `integer` | `query` | No | The starting index of the returned fields. Base index: 0. |
| `maxResults` | `integer` | `query` | No | The maximum number of fields to return per page, maximum allowed value is 100. |
| `fieldId` | `array` | `query` | No | The field IDs to filter by, if empty then all fields belonging to a field association scheme will be returned |
| `id` | `integer` | `path` | Yes | The scheme ID to search for child fields |

### Responses

#### 200 - Returns the matching fields, at the specified page of the results.

Example (application/json):
```json
"{\"allowedOperations\":[\"REMOVE\",\"CHANGE_REQUIRED\",\"CHANGE_DESCRIPTION\"],\"fieldId\":\"customfield_10000\",\"parameters\":{\"description\":\"text\",\"isRequired\":true,\"rendererType\":\"atlassian-wiki-renderer\"},\"restrictedToWorkTypes\":[\"1\",\"2\"],\"workTypeParameters\":[{\"description\":\"text\",\"isRequired\":true,\"rendererType\":\"jira-text-renderer\",\"workTypeId\":\"1\"},{\"description\":\"textarea\",\"isRequired\":false,\"rendererType\":\"atlassian-wiki-renderer\",\"workTypeId\":\"2\"}]}"
```

#### 400 - Returned if the request parameters are invalid (e.g., negative startAt, maxResults exceeding limit, duplicate fieldIds).

Schema (application/json):
```json
any
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
any
```

#### 403 - Returned if the user does not have the required permissions.

Schema (application/json):
```json
any
```

#### 404 - Returned if the feature flag is disabled or the scheme ID is not found.

Schema (application/json):
```json
any
```

