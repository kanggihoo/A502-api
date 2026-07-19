# 01-Update the GitLab for Jira (Forge) installation instance URL [PUT]

`PUT /api/v4/integrations/jira_forge/installation`

Sets the GitLab instance the installation points at. Omit instance_url (or send null) for GitLab.com. Requires a Jira site or organization admin.

### Request Body (application/json)

```json
{
  "instance_url": string, // Base URL of the self-managed GitLab instance; null for GitLab.com
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "success": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable entity

