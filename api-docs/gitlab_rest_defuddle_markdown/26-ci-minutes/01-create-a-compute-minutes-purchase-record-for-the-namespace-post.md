# 01-Create a compute minutes purchase record for the namespace [POST]

`POST /api/v4/namespaces/{id}/minutes`

Deprecated in GitLab 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Request Body (application/json)

```json
{
  "packs": [
    {
      "number_of_minutes": integer (required), // Number of additional minutes purchased
      "expires_at": string (required), // The expiry date for the purchase
      "purchase_xid": string (required), // Purchase ID for the additional minutes
    }
  ] (required), // An array of additional purchased minutes packs
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "namespace_id": integer,
  "expires_at": string,
  "number_of_minutes": integer,
  "purchase_xid": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

