# 25-Create context commits for a merge request [POST]

`POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/context_commits`

Creates context commits for a specified merge request.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project. |
| `merge_request_iid` | `integer` | `path` | Yes | The IID of a merge request |

### Request Body (application/json)

```json
{
  "commits": [
    string
  ] (required), // The context commits’ SHA.
}
```
### Responses

#### 201 - Created

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

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not found

