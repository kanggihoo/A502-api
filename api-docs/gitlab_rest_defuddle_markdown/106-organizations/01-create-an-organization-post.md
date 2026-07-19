# 01-Create an organization [POST]

`POST /api/v4/organizations`

Creates an organization. This feature was introduced in GitLab 17.5. This feature is behind the `allow_organization_creation` feature flag. In GitLab 18.3, the feature flag changed to `organization_switching`.

### Request Body (multipart/form-data)

```json
{
  "name": string (required), // The name of the organization
  "path": string (required), // The path of the organization
  "description": string, // The description of the organization
  "visibility": enum("private" | "public"), // The visibility level of the organization
  "avatar": string, // The avatar image for the organization
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "uuid": string,
  "name": string,
  "path": string,
  "description": string,
  "visibility": string,
  "created_at": string,
  "updated_at": string,
  "web_url": string,
  "avatar_url": string,
}
```

#### 400 - Bad Request

