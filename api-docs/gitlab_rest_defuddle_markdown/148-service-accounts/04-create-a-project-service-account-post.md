# 04-Create a project service account [POST]

`POST /api/v4/projects/{id}/service_accounts`

Creates a service account in a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "name": string, // Name of the user
  "username": string, // Username of the user
  "email": string, // Custom email address for the user
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "username": string,
  "public_email": string,
  "name": string,
  "email": string,
  "unconfirmed_email": string,
}
```

#### 400 - 400 Bad request

#### 401 - 401 Unauthorized

#### 403 - 403 Forbidden

#### 404 - 404 Project not found

