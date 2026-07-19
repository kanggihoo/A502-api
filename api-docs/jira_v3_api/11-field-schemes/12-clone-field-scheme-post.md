# 12-Clone field scheme [POST]

`POST /rest/api/3/config/fieldschemes/{id}/clone`

Endpoint for cloning an existing field association scheme into a new one.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the source field association scheme to clone from |

### Request Body (application/json)

```json
{
  "description": string, // Description of the scheme to be created
  "name": string (required), // The name of the scheme to be created
}
```
### Responses

#### 200 - Returned if the clone was successful.

Example (application/json):
```json
"{\"description\":\"Field association scheme description\",\"id\":10000,\"links\":{\"associations\":\"{BASE_API_URL}/rest/api/2/config/fieldschemes/9/fields\",\"projects\":\"{BASE_API_URL}/rest/api/2/config/fieldschemes/9/projects\"},\"name\":\"Field association scheme name\"}"
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

#### 404 - Returned if the feature flag is disabled or the source scheme ID is not found.

Schema (application/json):
```json
any
```

