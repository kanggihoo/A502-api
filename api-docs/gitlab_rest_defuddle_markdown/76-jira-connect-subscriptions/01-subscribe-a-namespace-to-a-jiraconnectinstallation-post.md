# 01-Subscribe a namespace to a JiraConnectInstallation [POST]

`POST /api/v4/integrations/jira_connect/subscriptions`

Subscribes the namespace to the JiraConnectInstallation

### Request Body (application/json)

```json
{
  "jwt": string (required), // JWT token for authorization with the Jira Connect installation
  "namespace_path": string (required), // Path for the namespace that should be subscribed
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "success": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

