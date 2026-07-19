# 03-Update the add-on purchase for the namespace [PUT]

`PUT /api/v4/namespaces/{id}/subscription_add_on_purchase/{add_on_name}`

Deprecated in GitLab 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |
| `add_on_name` | `any` | `path` | Yes |  |

### Request Body (application/json)

```json
{
  "started_on": string (required), // The date when purchase takes effect
  "expires_on": string (required), // The date when purchase expires on
  "quantity": integer, // The quantity of the purchase
  "purchase_xid": string, // The purchase identifier (example: the subscription name)
  "trial": boolean, // Whether the add-on is a trial
}
```
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

