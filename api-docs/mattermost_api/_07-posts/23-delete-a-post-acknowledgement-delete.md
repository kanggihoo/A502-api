# 23-Delete a post acknowledgement [DELETE]

`DELETE /api/v4/users/{user_id}/posts/{post_id}/ack`

Delete an acknowledgement form a post that you had previously acknowledged.
##### Permissions
Must have `read_channel` permission for the channel the post is in.<br/> Must be logged in as the user or have `edit_other_users` permission.<br/> The post must have been acknowledged in the previous 5 minutes.

__Minimum server version__: 7.7


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | User GUID |
| `post_id` | `string` | `path` | Yes | Post GUID |

### Responses

#### 200 - Acknowledgement deleted successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

