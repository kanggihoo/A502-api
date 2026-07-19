# 02-List all instance service accounts [GET]

`GET /api/v4/service_accounts`

Lists all instance service accounts. Use the `page` and `per_page` pagination parameters to filter the results.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

