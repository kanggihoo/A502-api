# 02-Apply multiple suggestions to a merge request [PUT]

`PUT /api/v4/suggestions/batch_apply`

Applies multiple suggested patches in a merge request. You must have the Developer, Maintainer, or Owner role.

### Request Body (application/json)

```json
{
  "ids": [
    integer
  ] (required), // An array of the suggestion IDs
  "commit_message": string, // A custom commit message to use instead of the default generated message or the project's default message
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "from_line": integer,
  "to_line": integer,
  "appliable": boolean,
  "applied": boolean,
  "from_content": string,
  "to_content": string,
}
```

#### 400 - Bad Request

