# 11-Delete a field scheme [DELETE]

`DELETE /rest/api/3/config/fieldschemes/{id}`

Delete a specified field association scheme

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the field association scheme to delete. |

### Responses

#### 200 - Returned if the field association scheme deletion was successful.

Example (application/json):
```json
"{\"deleted\":true,\"id\":\"10000\"}"
```

#### 400 - Returned if the scheme that the user is attempting to delete is a system scheme.

Schema (application/json):
```json
any
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

#### 404 - Return if the provided ID does not match any existing field association scheme

Schema (application/json):
```json
any
```

#### 409 - Return if the scheme that the user is attempting to delete is still in use.

Schema (application/json):
```json
any
```

