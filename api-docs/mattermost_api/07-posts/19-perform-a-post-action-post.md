# 19-Perform a post action [POST]

`POST /api/v4/posts/{post_id}/actions/{action_id}`

Perform a post action, which allows users to interact with integrations through posts.
##### Permissions
Must be authenticated and have the `read_channel` permission to the channel the post is in.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `post_id` | `string` | `path` | Yes | Post GUID |
| `action_id` | `string` | `path` | Yes | Action GUID |

### Responses

#### 200 - Post action successful

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 429 - The upstream integration rate-limited the request. The original status code is preserved so clients can honor retry semantics.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 502 - The upstream integration returned a 5xx (other than 503). Surfaced as Bad Gateway because the failure is upstream of Mattermost.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

#### 503 - The upstream integration is unavailable. The original status code is preserved so clients can honor retry semantics.

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

