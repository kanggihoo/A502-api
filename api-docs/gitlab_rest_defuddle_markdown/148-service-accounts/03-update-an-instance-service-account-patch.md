# 03-Update an instance service account [PATCH]

`PATCH /api/v4/service_accounts/{user_id}`

Updates a specified instance service account.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `integer` | `path` | Yes | The ID of the service account user |

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

#### 404 - 404 Not found

