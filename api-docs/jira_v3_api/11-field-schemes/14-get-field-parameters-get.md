# 14-Get field parameters [GET]

`GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters`

Retrieve field association parameters on a field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | the ID of the field association scheme to retrieve parameters for |
| `fieldId` | `string` | `path` | Yes | the ID of the field |

### Responses

#### 200 - Returned if the parameters fetched were successful.

Example (application/json):
```json
"{\"fieldId\":\"customfield_10000\",\"parameters\":{\"description\":\"Teams field\",\"isRequired\":true,\"rendererType\":\"atlassian-wiki-renderer\"},\"workTypeParameters\":[{\"description\":\"Teams field\",\"isRequired\":false,\"rendererType\":\"jira-text-renderer\",\"workTypeId\":10010}]}"
```

#### 400 - Returned if the request is invalid. If request is malformed, returns a collection of errors.

Schema (application/json):
```json
{}
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

Schema (application/json):
```json
any
```

#### 403 - Returned if the user does not have the required permissions

Schema (application/json):
```json
any
```

