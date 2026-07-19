# 03-Retrieve an application [GET]

`GET /api/v4/user/applications/{id}`

Retrieves details of a specific application owned by the authenticated user.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | ID of the application. Differs from the `application_id`. |

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

