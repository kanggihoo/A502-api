# 16-Validate a connection configuration [POST]

`POST /api/v4/oauth/outgoing_connections/validate`

Validate an outgoing OAuth connection. If an id is provided in the payload, and no client secret is provided, then the stored client secret is implicitly used for the validation.
__Minimum server version__: 9.6


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
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

#### 200 - The connection configuration is valid.

#### 400 - The connection configuration is invalid.

#### 401 - 

#### 404 - 

#### 500 - 

#### 501 - 

#### 502 - The connection configuration may be valid, but the server is unable to validate it upstream.

