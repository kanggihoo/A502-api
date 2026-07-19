# 33-List all members of a project [GET]

`GET /api/v4/projects/{id}/users`

Lists all members with access to a specified project.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `search` | `string` | `query` | No | Return list of users matching the search criteria |
| `skip_users` | `array` | `query` | No | Filter out users with the specified IDs |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "username": string,
  "public_email": string,
  "name": string,
  "state": string,
  "locked": boolean,
  "avatar_url": string,
  "avatar_path": string,
  "custom_attributes": [
    {
      "key": string,
      "value": string,
    }
  ],
  "web_url": string,
}
```

#### 400 - Bad Request

#### 403 - Unauthenticated

#### 404 - Not found

