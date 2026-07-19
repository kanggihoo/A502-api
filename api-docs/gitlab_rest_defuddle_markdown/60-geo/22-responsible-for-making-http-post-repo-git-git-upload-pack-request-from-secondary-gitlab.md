# 22-Responsible for making HTTP POST /repo.git/git-upload-pack
                  request from secondary gitlab-shell to primary [POST]

`POST /api/v4/geo/proxy_git_ssh/upload_pack`

Responsible for making HTTP POST /repo.git/git-upload-pack
                  request from secondary gitlab-shell to primary

### Request Body (application/json)

```json
{
  "secret_token": string (required), // Secret token used to authenticate requests from gitlab-shell                 to Geo proxy endpoints
  "data": {
    "gl_id": string (required), // ID of the user performing the operation
    "primary_repo": string (required), // Primary repository to clone or pull from
  } (required), // Object that contains the payload data for the Geo operation
  "output": string (required), // Output from git-upload-pack
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

#### 401 - 401 Unauthorized

