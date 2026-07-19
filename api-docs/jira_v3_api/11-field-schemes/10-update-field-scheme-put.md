# 10-Update field scheme [PUT]

`PUT /rest/api/3/config/fieldschemes/{id}`

Endpoint for updating an existing field association scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "description": string, // The description value to update
  "name": string, // The name value to update
}
```
### Responses

#### 200 - Returned if the update was successful.

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

#### 404 - Returned if the feature flag is disabled or the scheme ID is not found.

Schema (application/json):
```json
any
```

