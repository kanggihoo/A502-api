# 01-Get Jira instance info [GET]

`GET /rest/api/3/serverInfo`

Returns information about the Jira instance.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"baseUrl\":\"https://your-domain.atlassian.net\",\"buildDate\":\"2020-03-26T22:20:59.000+0000\",\"buildNumber\":582,\"defaultLocale\":{\"locale\":\"en_AU\"},\"displayUrl\":\"https://instance.jira.your-domain.com\",\"displayUrlConfluence\":\"https://instance.confluence.your-domain.com\",\"displayUrlServicedeskHelpCenter\":\"https://instance.help.your-domain.com\",\"scmInfo\":\"1f51473f5c7b75c1a69a0090f4832cdc5053702a\",\"serverTime\":\"2020-03-31T16:43:50.000+0000\",\"serverTimeZone\":\"Australia/Sydney\",\"serverTitle\":\"My Jira instance\",\"version\":\"1001.0.0-SNAPSHOT\",\"versionNumbers\":[5,0,0]}"
```

#### 401 - Returned if the authentication credentials are incorrect.

