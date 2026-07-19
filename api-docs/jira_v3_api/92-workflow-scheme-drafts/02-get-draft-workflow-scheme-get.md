# 02-Get draft workflow scheme [GET]

`GET /rest/api/3/workflowscheme/{id}/draft`

Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.  
Note that:

 *  Only active workflow schemes can have draft workflow schemes.
 *  An active workflow scheme can only have one draft workflow scheme.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the active workflow scheme that the draft was created from. |

### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultWorkflow\":\"scrum workflow\",\"description\":\"The description of the example workflow scheme.\",\"draft\":true,\"id\":17218781,\"issueTypeMappings\":{\"10000\":\"jira\",\"10001\":\"jira\"},\"lastModified\":\"Today 6:38 PM\",\"lastModifiedUser\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":true,\"applicationRoles\":{\"items\":[],\"size\":1},\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"groups\":{\"items\":[],\"size\":3},\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"name\":\"Example workflow scheme\",\"originalDefaultWorkflow\":\"jira\",\"originalIssueTypeMappings\":{\"10001\":\"builds workflow\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft\"}"
```

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if:

 *  the original active workflow scheme is not found.
 *  the original active workflow scheme does not have a draft.

