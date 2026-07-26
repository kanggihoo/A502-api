# 28-Get client license [GET]

`GET /api/v4/license/client`

Get a subset of the server license needed by the client.
##### Permissions
No permission required but having the `manage_system` permission returns more information.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `format` | `string` | `query` | Yes | Must be `old`, other formats not implemented yet |

### Responses

#### 200 - License retrieval successful

#### 400 - 

#### 501 - 

