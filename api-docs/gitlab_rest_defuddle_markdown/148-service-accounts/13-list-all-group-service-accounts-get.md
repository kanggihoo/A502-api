# 13-List all group service accounts [GET]

`GET /api/v4/groups/{id}/service_accounts`

Lists all service accounts in a specified group. Use the `page` and `per_page` pagination parameters to filter the results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the group |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `order_by` | `string` | `query` | No | Attribute to sort by |
| `sort` | `string` | `query` | No | Order of sorting |

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

#### 404 - 404 Group not found

