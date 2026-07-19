# 04-Creates a storage limit exclusion for a Namespace [POST]

`POST /api/v4/namespaces/{id}/storage/limit_exclusion`

Creates a Namespaces::Storage::LimitExclusion

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Request Body (application/json)

```json
{
  "reason": string (required), // The reason the Namespace is being excluded
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "namespace_id": integer,
  "namespace_name": string,
  "reason": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

