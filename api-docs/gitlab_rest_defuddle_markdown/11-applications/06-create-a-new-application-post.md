# 06-Create a new application [POST]

`POST /api/v4/applications`

This feature was introduced in GitLab 10.5

### Request Body (application/json)

```json
{
  "name": string (required), // Name of the application.
  "redirect_uri": string (required), // Redirect URI of the application.
  "scopes": string (required), // Scopes of the application. You can specify multiple scopes by separating\                                  each scope using a space
  "confidential": boolean, // The application is used where the client secret can be kept confidential. Native mobile apps \                         and Single Page Apps are considered non-confidential. Defaults to true if not supplied
}
```
### Responses

#### 200 - OK

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

