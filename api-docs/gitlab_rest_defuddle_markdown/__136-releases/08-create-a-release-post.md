# 08-Create a release [POST]

`POST /api/v4/projects/{id}/releases`

Creates a release. Developer level access to the project is required to create a release.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | The ID or URL-encoded path of the project |

### Request Body (application/json)

```json
{
  "tag_name": string (required), // The tag where the release is created from
  "tag_message": string, // Message to use if creating a new annotated tag
  "name": string, // The release name
  "description": string, // The description of the release. You can use Markdown
  "ref": string, // If a tag specified in `tag_name` doesn't exist, the release is created from `ref` and tagged with `tag_name`. It can be a commit SHA, another tag name, or a branch name.
  "assets": {
    "links": [
      {
        "name": string (required), // The name of the link. Link names must be unique within the release
        "url": string (required), // The URL of the link. Link URLs must be unique within the release
        "direct_asset_path": string, // Optional path for a direct asset link
        "filepath": string, // Deprecated: optional path for a direct asset link
        "link_type": string, // The type of the link: `other`, `runbook`, `image`, `package`. Defaults to `other`
      }
    ], // Link information about the release
  }, // Object that contains assets for the release
  "milestones": [
    string
  ], // The title of each milestone the release is associated with. GitLab Premium customers can specify group milestones. Cannot be combined with `milestone_ids` parameter.
  "milestone_ids": any,
  "released_at": string, // Date and time for the release. Defaults to the current time. Expected in ISO 8601 format (`2019-03-15T08:00:00Z`). Only provide this field if creating an upcoming or historical release.
  "legacy_catalog_publish": boolean, // If true, the release will be published to the CI catalog. This parameter is for internal use only and will be removed in a future release. If the feature flag ci_release_cli_catalog_publish_option is disabled, this parameter will be ignored and the release will published to the CI catalog as it was before this parameter was introduced.
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "name": string,
  "tag_name": string,
  "description": string,
  "created_at": string,
  "released_at": string,
  "upcoming_release": boolean,
  "description_html": string,
  "author": {
    "id": integer,
    "username": string,
    "public_email": string,
    "name": string,
    "state": string,
    "locked": boolean,
    "avatar_url": string,
    "avatar_path": string,
    "custom_attributes": [
      {
        "key": string,
        "value": string,
      }
    ],
    "web_url": string,
  },
  "commit": {
    "id": string,
    "short_id": string,
    "created_at": string,
    "parent_ids": [
      string
    ],
    "title": string,
    "message": string,
    "author_name": string,
    "author_email": string,
    "authored_date": string,
    "committer_name": string,
    "committer_email": string,
    "committed_date": string,
    "trailers": {},
    "extended_trailers": {},
    "web_url": string,
  },
  "milestones": {
    "id": integer,
    "iid": integer,
    "project_id": integer,
    "group_id": string,
    "title": string,
    "description": string,
    "state": string,
    "created_at": string,
    "updated_at": string,
    "due_date": string,
    "start_date": string,
    "expired": boolean,
    "web_url": string,
    "issue_stats": {},
  },
  "commit_path": string,
  "tag_path": string,
  "assets": string,
  "evidences": {
    "sha": string,
    "filepath": string,
    "collected_at": string,
  },
  "_links": string,
}
```

#### 400 - Bad request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 404 - Not found

#### 409 - Conflict

#### 422 - Unprocessable entity

