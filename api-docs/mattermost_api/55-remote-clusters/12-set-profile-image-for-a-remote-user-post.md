# 12-Set profile image for a remote user. [POST]

`POST /api/v4/remotecluster/{user_id}/image`

Uploads and sets a profile image for a remote user managed by the
requesting remote cluster. This endpoint is authenticated with a
remote-cluster token.

##### Permissions
No user session permissions required.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The remote user ID. |

### Request Body (multipart/form-data)

```json
{
  "image": string,
}
```
### Responses

#### 200 - Profile image updated successfully

#### 400 - 

#### 401 - 

