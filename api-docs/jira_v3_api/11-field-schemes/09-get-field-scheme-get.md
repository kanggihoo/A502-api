# 09-Get field scheme [GET]

`GET /rest/api/3/config/fieldschemes/{id}`

Endpoint for fetching a field association scheme by its ID

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The scheme id to fetch |

### Responses

#### 200 - Returned if a field association scheme matches the given scheme ID

Example (application/json):
```json
"{\"description\":\"This is a field association scheme\",\"fieldsCount\":5,\"id\":\"123\",\"isDefault\":false,\"links\":{\"associations\":\"rest/api/3/config/fieldschemes/10000/fields\",\"projects\":\"rest/api/3/config/fieldschemes/10000/projects\"},\"name\":\"Scheme\"}"
```

#### 403 - Returned if the user does not have the required permissions

Schema (application/json):
```json
any
```

#### 404 - Returned if provided ID does not match any field association schemes

Schema (application/json):
```json
any
```

