# 05-Add a GPG key for a user [POST]

`POST /api/v4/users/{id}/gpg_keys`

Adds a GPG key for a specified user account. Administrators only.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the user |

### Request Body (application/json)

```json
{
  "key": string (required), // The new GPG key
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "key": string,
  "created_at": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

