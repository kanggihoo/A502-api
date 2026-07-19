# 02-Set project's sender email [PUT]

`PUT /rest/api/3/project/{projectId}/email`

Sets the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

If `emailAddress` is an empty string, the default email address is restored.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `integer` | `path` | Yes | The project ID. |

### Request Body (application/json)

```json
{
  "emailAddress": string, // The email address.
  "emailAddressStatus": [
    string
  ], // When using a custom domain, the status of the email address.
}
```
### Responses

#### 204 - Returned if the project's sender email address is successfully set.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is not valid, if the email address is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have permission to administer the project.

#### 404 - Returned if the project is not found.

