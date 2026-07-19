# 02-Create a project alias [POST]

`POST /api/v4/project_aliases`

Creates a project alias.

### Request Body (application/json)

```json
{
  "project_id": string (required), // The ID or URL-encoded path of the project
  "name": string (required), // The alias of the project
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "id": integer,
  "project_id": integer,
  "name": string,
}
```

#### 400 - Bad request

#### 403 - Forbidden

#### 404 - Not found

