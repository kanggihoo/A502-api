# 15-Add a GPG key [POST]

`POST /api/v4/user/gpg_keys`

Adds a GPG key for the currently authenticated user.

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

