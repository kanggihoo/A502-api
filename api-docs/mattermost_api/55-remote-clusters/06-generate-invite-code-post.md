# 06-Generate invite code. [POST]

`POST /api/v4/remotecluster/{remote_id}/generate_invite`

Generates an invite code for a given remote cluster.

##### Permissions
`manage_secure_connections`


### Request Body (application/json)

```json
{
  "password": string (required), // The password to encrypt the invite code with.
}
```
### Responses

#### 201 - Invite code generated

Schema (application/json):
```json
string
```

#### 401 - 

#### 403 - 

