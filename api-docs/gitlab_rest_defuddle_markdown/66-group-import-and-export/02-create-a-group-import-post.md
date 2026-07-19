# 02-Create a group import [POST]

`POST /api/v4/groups/import`

Creates a group import. The maximum import file size can be set by the Administrator on GitLab Self-Managed (defaults to `0` (unlimited)).

### Request Body (multipart/form-data)

```json
{
  "path": string (required), // Group path
  "name": string (required), // Group name
  "file": string (required), // The group export file to be imported
  "parent_id": integer, // The ID of the parent group that the group will be imported into. Defaults to the current user's namespace.
  "organization_id": integer, // The ID of the organization that the group will be part of. 
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 503 - Service unavailable

