# 02-Register the GitLab for Jira (Forge) system token for direct dev-info sync [POST]

`POST /api/v4/integrations/jira_forge/installation/forge_token`

Stores the Forge app system OAuth token (X-Forge-Oauth-System header) and the Jira apiBaseUrl (from the FIT), so GitLab pushes dev-info directly to Jira. See Atlassian::Forge::SystemTokenClient.

### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "success": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 422 - Unprocessable entity

