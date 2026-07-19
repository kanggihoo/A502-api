# 02-List workflow history entries [POST]

`POST /rest/api/3/workflow/history/list`

Returns a list of workflow history entries for a specified workflow id.

**Note:** Stored workflow data expires after 60 days. Additionally, no data from before the 30th of October 2025 is available.

**[Permissions](#permissions) required:**

 *  *Administer Jira* global permission to access all, including project-scoped, workflows
 *  At least one of the *Administer projects* and *View (read-only) workflow* project permissions to access project-scoped workflows

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `expand` | `string` | `query` | No | Use [expand](#expansion) to include additional information in the response. This parameter accepts a comma-separated list. Expand options include:<br><br> *  `includeIntermediateWorkflows` Includes intermediate workflow versions that are sometimes created during workflow updates or migrations. By default, these are omitted from the response. |

### Request Body (application/json)

```json
{
  "workflowId": string, // The id of the workflow to read the history for.
}
```
### Responses

#### 200 - Returned if the request is successful.

Example (application/json):
```json
"{\"entries\":[{\"isIntermediate\":false,\"workflowId\":\"c5ef565c-1b1e-427e-bc3b-e677b0dc027c\",\"workflowVersion\":4,\"writtenAt\":\"2025-11-20 02:21:19.598\"},{\"isIntermediate\":true,\"workflowId\":\"c5ef565c-1b1e-427e-bc3b-e677b0dc027c\",\"workflowVersion\":3,\"writtenAt\":\"2025-11-19 02:23:17.465\"}]}"
```

#### 400 - Returned if the request is not valid.

#### 401 - Returned if the authentication credentials are incorrect or missing, or the caller doesn't have permissions to perform the operation.

