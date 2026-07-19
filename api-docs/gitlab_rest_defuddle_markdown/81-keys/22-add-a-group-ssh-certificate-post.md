# 22-Add a group SSH certificate [POST]

`POST /api/v4/groups/{id}/ssh_certificates`

Adds a group SSH certificate for a specified group.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |

### Request Body (application/json)

```json
{
  "title": string (required), // The title of the ssh certificate
  "key": string (required), // The key of the ssh certificate
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "title": string,
  "key": string,
  "created_at": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

