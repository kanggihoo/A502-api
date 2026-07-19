# 23-Responsible for making HTTP GET /repo.git/info/refs?service=git-receive-pack
                  request from secondary gitlab-shell to primary [POST]

`POST /api/v4/geo/proxy_git_ssh/info_refs_receive_pack`

Responsible for making HTTP GET /repo.git/info/refs?service=git-receive-pack
                  request from secondary gitlab-shell to primary

### Request Body (application/json)

```json
{
  "secret_token": string (required), // Secret token used to authenticate requests from gitlab-shell                 to Geo proxy endpoints
  "data": {
    "gl_id": string (required), // ID of the user performing the operation
    "primary_repo": string (required), // Primary repository to push to
  } (required), // Object that contains the payload data for the Geo operation
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - 401 Unauthorized

