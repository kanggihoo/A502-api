# 04-Update a connection [PUT]

`PUT /api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}`

Update an outgoing OAuth connection.
__Minimum server version__: 9.6


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `outgoing_oauth_connection_id` | `string` | `path` | Yes | Outgoing OAuth connection ID |
| `team_id` | `string` | `query` | Yes | Current Team ID in integrations backstage |

### Request Body (application/json)

```json
{
  "name": string, // The name of the outgoing OAuth connection.
  "client_id": string, // The client ID of the outgoing OAuth connection.
  "client_secret": string, // The client secret of the outgoing OAuth connection.
  "credentials_username": string, // The username of the credentials of the outgoing OAuth connection.
  "credentials_password": string, // The password of the credentials of the outgoing OAuth connection.
  "oauth_token_url": string, // The OAuth token URL of the outgoing OAuth connection.
  "grant_type": string, // The grant type of the outgoing OAuth connection.
  "audiences": string, // The audiences of the outgoing OAuth connection.
}
```
### Responses

#### 200 - Successfully updated outgoing OAuth connection

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

#### 400 - 

#### 401 - 

#### 404 - 

#### 500 - 

#### 501 - 

