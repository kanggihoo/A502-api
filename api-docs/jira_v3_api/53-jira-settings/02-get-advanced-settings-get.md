# 02-Get advanced settings [GET]

`GET /rest/api/3/application-properties/advanced-settings`

Returns the application properties that are accessible on the *Advanced Settings* page. To navigate to the *Advanced Settings* page in Jira, choose the Jira icon > **Jira settings** > **System**, **General Configuration** and then click **Advanced Settings** (in the upper right).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"[{\"defaultValue\":\"\",\"desc\":\"Jira home directory\",\"id\":\"jira.home\",\"key\":\"jira.home\",\"name\":\"jira.home\",\"type\":\"string\",\"value\":\"/var/jira/jira-home\"},{\"defaultValue\":\"CLONE -\",\"id\":\"jira.clone.prefix\",\"key\":\"jira.clone.prefix\",\"name\":\"The prefix added to the Summary field of cloned issues\",\"type\":\"string\",\"value\":\"CLONE -\"}]"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user is not an administrator.

