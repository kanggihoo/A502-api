# 15-Update a group service account [PATCH]

`PATCH /api/v4/groups/{id}/service_accounts/{user_id}`

Update a specified group service account.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `user_id` | `integer` | `path` | Yes | The ID of the service account |

### Request Body (application/json)

```json
{
  "name": string, // Name of the user
  "username": string, // Username of the user
  "email": string, // Custom email address for the user
}
```
### Responses

#### 200 - OK

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

#### 404 - 404 User not found

