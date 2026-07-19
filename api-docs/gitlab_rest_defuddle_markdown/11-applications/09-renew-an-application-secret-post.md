# 09-Renew an application secret [POST]

`POST /api/v4/applications/{id}/renew-secret`

Renew the secret of a specific application

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the application (not the application_id) |

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

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

