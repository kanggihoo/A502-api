# 01-Retrieve the public signing key [GET]

`GET /api/v4/web_commits/public_key`

Retrieves the GitLab public key for signing web commits. This feature was introduced in GitLab 17.4.

### Responses

#### 200 - OK

#### 404 - Public key not found.

#### 503 - The git server, Gitaly, is not available at this time. Please contact your administrator.

