# 02-Returns an add-on purchase for the namespace [GET]

`GET /api/v4/namespaces/{id}/subscription_add_on_purchase/{add_on_name}`

Deprecated in GitLab 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |
| `add_on_name` | `any` | `path` | Yes |  |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "namespace_id": integer,
  "namespace_name": string,
  "add_on": string,
  "quantity": integer,
  "started_on": string,
  "expires_on": string,
  "purchase_xid": string,
  "trial": boolean,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

