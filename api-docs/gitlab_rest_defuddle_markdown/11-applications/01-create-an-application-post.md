# 01-Create an application [POST]

`POST /api/v4/user/applications`

Creates a new OAuth application for the authenticated user. This feature was introduced in GitLab 19.0

### Request Body (application/json)

```json
{
  "name": string (required), // Name of the application.
  "redirect_uri": string (required), // Redirect URI of the application.
  "scopes": string (required), // Scopes available to the application. Separate multiple scopes with a space.
  "confidential": boolean, // If `true`, the application can securely store client credentials, such as the client secret. Non-confidential applications, such as native mobile apps and Single Page Apps might expose client credentials. If unset, defaults to `true`.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "application_id": string,
  "application_name": string,
  "callback_url": string,
  "confidential": boolean,
  "scopes": [
    any
  ],
  "secret": string,
}
```

#### 400 - Bad Request

