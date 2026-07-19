# 04-Update group level notification level settings, defaults to Global [PUT]

`PUT /api/v4/groups/{id}/notification_settings`

This feature was introduced in GitLab 8.12

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The group ID |

### Request Body (application/json)

```json
{
  "level": string, // The group notification level
  "new_release": boolean, // Enable/disable this notification
  "new_note": boolean, // Enable/disable this notification
  "new_issue": boolean, // Enable/disable this notification
  "reopen_issue": boolean, // Enable/disable this notification
  "close_issue": boolean, // Enable/disable this notification
  "reassign_issue": boolean, // Enable/disable this notification
  "issue_due": boolean, // Enable/disable this notification
  "new_merge_request": boolean, // Enable/disable this notification
  "push_to_merge_request": boolean, // Enable/disable this notification
  "reopen_merge_request": boolean, // Enable/disable this notification
  "close_merge_request": boolean, // Enable/disable this notification
  "reassign_merge_request": boolean, // Enable/disable this notification
  "change_reviewer_merge_request": boolean, // Enable/disable this notification
  "merge_merge_request": boolean, // Enable/disable this notification
  "failed_pipeline": boolean, // Enable/disable this notification
  "fixed_pipeline": boolean, // Enable/disable this notification
  "success_pipeline": boolean, // Enable/disable this notification
  "moved_project": boolean, // Enable/disable this notification
  "merge_when_pipeline_succeeds": boolean, // Enable/disable this notification
  "new_epic": boolean, // Enable/disable this notification
  "service_account_failed_pipeline": boolean, // Enable/disable this notification
  "service_account_success_pipeline": boolean, // Enable/disable this notification
  "service_account_fixed_pipeline": boolean, // Enable/disable this notification
}
```
### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "level": string,
  "events": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 404 - Not Found

