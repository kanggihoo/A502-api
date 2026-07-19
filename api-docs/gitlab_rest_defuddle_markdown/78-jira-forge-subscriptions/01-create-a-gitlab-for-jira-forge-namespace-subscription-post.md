# 01-Create a GitLab for Jira (Forge) namespace subscription [POST]

`POST /api/v4/integrations/jira_forge/subscriptions`

Subscribes a GitLab namespace to the Forge installation so its development data syncs to Jira. Authenticated as the GitLab user (OAuth); the Jira installation and user are resolved from the Forge invocation context.

### Request Body (application/json)

```json
{
  "namespace_path": string (required), // Path of the namespace to subscribe
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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 422 - Unprocessable entity

