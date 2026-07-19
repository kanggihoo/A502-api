# 09-Set workflow for issue type in draft workflow scheme [PUT]

`PUT /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}`

Sets the workflow for an issue type in a workflow scheme's draft.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `integer` | `path` | Yes | The ID of the workflow scheme that the draft belongs to. |
| `issueType` | `string` | `path` | Yes | The ID of the issue type. |

### Request Body (application/json)

```json
{
  "issueType": string, // The ID of the issue type. Not required if updating the issue type-workflow mapping.
  "updateDraftIfNeeded": boolean, // Set to true to create or update the draft of a workflow scheme and update the mapping in the draft, when the workflow scheme cannot be edited. Defaults to `false`. Only applicable when updating the workflow-issue types mapping.
  "workflow": string, // The name of the workflow.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"defaultWorkflow\":\"scrum workflow\",\"description\":\"The description of the example workflow scheme.\",\"draft\":true,\"id\":17218781,\"issueTypeMappings\":{\"10000\":\"jira\",\"10001\":\"jira\"},\"lastModified\":\"Today 6:38 PM\",\"lastModifiedUser\":{\"accountId\":\"5b10a2844c20165700ede21g\",\"accountType\":\"atlassian\",\"active\":true,\"applicationRoles\":{\"items\":[],\"size\":1},\"avatarUrls\":{\"16x16\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16\",\"24x24\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24\",\"32x32\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32\",\"48x48\":\"https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48\"},\"displayName\":\"Mia Krystof\",\"emailAddress\":\"mia@example.com\",\"groups\":{\"items\":[],\"size\":3},\"key\":\"\",\"name\":\"\",\"self\":\"https://your-domain.atlassian.net/rest/api/3/user?accountId=5b10a2844c20165700ede21g\",\"timeZone\":\"Australia/Sydney\"},\"name\":\"Example workflow scheme\",\"originalDefaultWorkflow\":\"jira\",\"originalIssueTypeMappings\":{\"10001\":\"builds workflow\"},\"self\":\"https://your-domain.atlassian.net/rest/api/3/workflowscheme/17218781/draft\"}"
```

#### 400 - Returned if the request is invalid.

#### 401 - Returned if the authentication credentials are incorrect or missing.

#### 403 - Returned if the user does not have the necessary permission.

#### 404 - Returned if the workflow scheme or issue type is not found.

