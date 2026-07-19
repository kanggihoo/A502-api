# 05-Delete a connection [DELETE]

`DELETE /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}`

Delete an outgoing OAuth connection.
__Minimum server version__: 9.6


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `outgoing_oauth_connection_id` | `string` | `path` | Yes | Outgoing OAuth connection ID |
| `team_id` | `string` | `query` | Yes | Current Team ID in integrations backstage |

### Responses

#### 200 - Successfully deleted outgoing OAuth connection

#### 401 - 

#### 404 - 

#### 500 - 

#### 501 - 

