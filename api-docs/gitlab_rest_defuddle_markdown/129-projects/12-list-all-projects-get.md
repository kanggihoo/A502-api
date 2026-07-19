# 12-List all projects [GET]

`GET /api/v4/projects`

Lists all projects. Unauthenticated requests return only public projects with a limited subset of attributes. You can filter responses by custom attributes.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `order_by` | `string` | `query` | No | Return projects ordered by field. storage_size, repository_size, wiki_size, packages_size are only available to admins. Similarity is available when searching and is limited to projects the user has access to. |
| `sort` | `string` | `query` | No | Return projects sorted in ascending and descending order |
| `archived` | `boolean` | `query` | No | Limit by archived status |
| `visibility` | `string` | `query` | No | Limit by visibility |
| `search` | `string` | `query` | No | Return list of projects matching the search criteria |
| `search_namespaces` | `boolean` | `query` | No | Include ancestor namespaces when matching search criteria |
| `owned` | `boolean` | `query` | No | Limit by owned by authenticated user |
| `starred` | `boolean` | `query` | No | Limit by starred status |
| `imported` | `boolean` | `query` | No | Limit by imported by authenticated user |
| `membership` | `boolean` | `query` | No | Limit by projects that the current user is a member of |
| `with_issues_enabled` | `boolean` | `query` | No | Limit by enabled issues feature |
| `with_merge_requests_enabled` | `boolean` | `query` | No | Limit by enabled merge requests feature |
| `with_programming_language` | `string` | `query` | No | Limit to repositories which use the given programming language |
| `min_access_level` | `integer` | `query` | No | Limit by minimum access level of authenticated user |
| `id_after` | `integer` | `query` | No | Limit results to projects with IDs greater than the specified ID |
| `id_before` | `integer` | `query` | No | Limit results to projects with IDs less than the specified ID |
| `last_activity_after` | `string` | `query` | No | Limit results to projects with last_activity after specified time. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `last_activity_before` | `string` | `query` | No | Limit results to projects with last_activity before specified time. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `repository_storage` | `string` | `query` | No | Which storage shard the repository is on. Available only to admins |
| `topic` | `array` | `query` | No | Comma-separated list of topics. Limit results to projects having all topics |
| `topic_id` | `integer` | `query` | No | Limit results to projects with the assigned topic given by the topic ID |
| `updated_before` | `string` | `query` | No | Return projects updated before the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `updated_after` | `string` | `query` | No | Return projects updated after the specified datetime. Format: ISO 8601 YYYY-MM-DDTHH:MM:SSZ |
| `include_pending_delete` | `boolean` | `query` | No | Include projects in pending delete state. Can only be set by admins |
| `marked_for_deletion_on` | `string` | `query` | No | Date when the project was marked for deletion |
| `active` | `boolean` | `query` | No | Limit by projects that are not archived and not marked for deletion |
| `wiki_checksum_failed` | `boolean` | `query` | No | Limit by projects where wiki checksum is failed |
| `repository_checksum_failed` | `boolean` | `query` | No | Limit by projects where repository checksum is failed |
| `include_hidden` | `boolean` | `query` | No | Include hidden projects. Can only be set by admins |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `simple` | `boolean` | `query` | No | Return only the ID, URL, name, and path of each project |
| `statistics` | `boolean` | `query` | No | Include project statistics |
| `with_custom_attributes` | `boolean` | `query` | No | Include custom attributes in the response |
| `custom_attributes` | `object` | `query` | No | Filter with custom attributes |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "description": string,
  "name": string,
  "name_with_namespace": string,
  "path": string,
  "path_with_namespace": string,
  "created_at": string,
  "default_branch": string,
  "tag_list": [
    string
  ],
  "topics": [
    string
  ],
  "ssh_url_to_repo": string,
  "http_url_to_repo": string,
  "web_url": string,
  "readme_url": string,
  "forks_count": integer,
  "license_url": string,
  "license": {
    "key": string,
    "name": string,
    "nickname": string,
    "html_url": string,
    "source_url": string,
  },
  "avatar_url": string,
  "star_count": integer,
  "last_activity_at": string,
  "visibility": string,
  "namespace": {
    "id": integer,
    "name": string,
    "path": string,
    "kind": string,
    "full_path": string,
    "parent_id": integer,
    "avatar_url": string,
    "web_url": string,
  },
  "custom_attributes": {
    "key": string,
    "value": string,
  },
  "repository_storage": string,
}
```

#### 400 - Bad request

