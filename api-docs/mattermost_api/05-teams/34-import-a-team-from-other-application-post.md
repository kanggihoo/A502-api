# 34-Import a Team from other application [POST]

`POST /api/v4/teams/{team_id}/import`

Import a team into a existing team. Import users, channels, posts, hooks.
##### Permissions
Must have `permission_import_team` permission.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Request Body (multipart/form-data)

```json
{
  "file": string (required), // A file to be uploaded in zip format.
  "filesize": integer (required), // The size of the zip file to be imported.
  "importFrom": string (required), // String that defines from which application the team was exported to be imported into Mattermost.
}
```
### Responses

#### 200 - JSON object containing a base64 encoded text file of the import logs in its `results` property.

Schema (application/json):
```json
{
  "results": string,
}
```

#### 400 - 

#### 403 - 

