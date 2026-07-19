# 01-Import GitHub gists into GitLab snippets [POST]

`POST /api/v4/import/github/gists`

Imports personal GitHub gists into GitLab snippets. You can import gists with up to 10 files. GitHub gists with more than 10 files are skipped. You should manually migrate these GitHub gists. If any gists cannot be imported, an email is sent with a list of gists that were not imported.

### Request Body (application/json)

```json
{
  "personal_access_token": string (required), // GitHub personal access token
}
```
### Responses

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 422 - Unprocessable Entity

#### 429 - Too Many Requests

