# 08-Get the common ancestor between commits [GET]

`GET /api/v4/projects/{id}/repository/merge_base`

Get the common ancestor between commits

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |
| `refs` | `array` | `query` | Yes | The refs to find the common ancestor of, multiple refs can be passed |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": string,
  "short_id": string,
  "created_at": string,
  "parent_ids": [
    string
  ],
  "title": string,
  "message": string,
  "author_name": string,
  "author_email": string,
  "authored_date": string,
  "committer_name": string,
  "committer_email": string,
  "committed_date": string,
  "trailers": {},
  "extended_trailers": {},
  "web_url": string,
}
```

#### 400 - Bad Request

#### 404 - Not Found

