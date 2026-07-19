# 02-Create an agent URL configuration [POST]

`POST /api/v4/projects/{id}/cluster_agents/{agent_id}/url_configurations`

Creates an agent URL configuration. You must have the Maintainer or Owner role to use this endpoint. An agent can have only one URL configuration at the time. This feature was introduced in GitLab 17.4.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `agent_id` | `integer` | `path` | Yes | The ID of an agent |

### Request Body (application/json)

```json
{
  "url": string (required), // The url where the receptive agent is listening
  "client_cert": string, // The client certificate in PEM format for mTLS
  "client_key": string, // The client key in PEM format for mTLS
  "ca_cert": string, // The CA certificate in PEM format for TLS validation
  "tls_host": string, // The host name for TLS validation
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "agent_id": integer,
  "url": string,
  "public_key": string,
  "client_cert": string,
  "ca_cert": string,
  "tls_host": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

