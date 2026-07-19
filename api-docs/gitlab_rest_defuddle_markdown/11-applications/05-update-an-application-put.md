# 05-Update an application [PUT]

`PUT /api/v4/user/applications/{id}`

Updates an existing application owned by the authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the application. Differs from the `application_id`. |

### Request Body (application/json)

```json
{
  "name": string, // Name of the application.
  "scopes": string, // Scopes available to the application. Separate multiple scopes with a space.
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
}
```

#### 400 - Bad Request

#### 404 - Not Found

