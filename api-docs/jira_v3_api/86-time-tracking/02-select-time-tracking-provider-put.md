# 02-Select time tracking provider [PUT]

`PUT /rest/api/3/configuration/timetracking`

Selects a time tracking provider.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "key": string (required), // The key for the time tracking provider. For example, *JIRA*.
  "name": string, // The name of the time tracking provider. For example, *JIRA provided time tracking*.
  "url": string, // The URL of the configuration page for the time tracking provider app. For example, */example/config/url*. This property is only returned if the `adminPageKey` property is set in the module descriptor of the time tracking provider app.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the time tracking provider is not found.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

