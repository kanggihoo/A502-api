# 13-Get a connection [GET]

`GET /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}`

Retrieve an outgoing OAuth connection.
__Minimum server version__: 9.6


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `outgoing_oauth_connection_id` | `string` | `path` | Yes | Outgoing OAuth connection ID |
| `team_id` | `string` | `query` | Yes | Current Team ID in integrations backstage |

### Responses

#### 200 - Successfully fetched outgoing OAuth connection

Schema (application/json):
```json
{
  "id": string, // The unique identifier for the outgoing OAuth connection.
  "name": string, // The name of the outgoing OAuth connection.
  "create_at": integer, // The time in milliseconds the outgoing OAuth connection was created.
  "update_at": integer, // The time in milliseconds the outgoing OAuth connection was last updated.
  "grant_type": string, // The grant type of the outgoing OAuth connection.
  "audiences": string, // The audiences of the outgoing OAuth connection.
}
```

#### 401 - 

#### 500 - 

#### 501 - 

