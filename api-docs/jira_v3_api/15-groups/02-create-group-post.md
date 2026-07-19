# 02-Create group [POST]

`POST /rest/api/3/group`

Creates a group.

**[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

### Request Body (application/json)

```json
{
  "name": string (required), // The name of the group.
}
```
### Responses

#### 201 - Returned if the request is successful.

Example (application/json):
```json
"{\"expand\":\"users\",\"groupId\":\"276f955c-63d7-42c8-9520-92d01dca0625\",\"name\":\"power-users\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/group?groupId=276f955c-63d7-42c8-9520-92d01dca0625\",\"users\":{\"end-index\":0,\"items\":[{\"accountId\":\"5b10a2844c20165700ede21g\",\"active\":false,\"displayName\":\"Mia Krystof\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\"}],\"max-results\":50,\"size\":1,\"start-index\":0}}"
```

#### 400 - Returned if group name is not specified or the group name is in use.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

