# 07-List all namespaces [GET]

`GET /api/v4/namespaces`

Lists all namespaces available to the current user. If the user is an administrator, this endpoint returns all namespaces in the instance.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `search` | `string` | `query` | No | Returns a list of namespaces the user is authorized to view based on the search criteria |
| `owned_only` | `boolean` | `query` | No | In GitLab 14.2 and later, returns a list of owned namespaces only |
| `top_level_only` | `boolean` | `query` | No | Only include top level namespaces |
| `full_path_search` | `boolean` | `query` | No | If `true`, the `search` parameter is matched against the full path of the namespaces |
| `page` | `integer` | `query` | No | Current page number |
| `per_page` | `integer` | `query` | No | Number of items per page |
| `requested_hosted_plan` | `string` | `query` | No | Name of the hosted plan requested by the customer |

### Responses

#### 200 - OK

Schema (application/json):
```json
{
  "id": integer,
  "name": string,
  "path": string,
  "kind": string,
  "full_path": string,
  "parent_id": integer,
  "avatar_url": string,
  "web_url": string,
  "members_count_with_descendants": integer,
  "root_repository_size": integer,
  "projects_count": integer,
  "shared_runners_minutes_limit": integer,
  "extra_shared_runners_minutes_limit": integer,
  "additional_purchased_storage_size": integer,
  "additional_purchased_storage_ends_on": string,
  "billable_members_count": integer,
  "seats_in_use": integer,
  "max_seats_used": integer,
  "max_seats_used_changed_at": string,
  "end_date": string,
  "plan": string,
  "trial_ends_on": string,
  "trial": boolean,
}
```

#### 400 - Bad Request

#### 401 - Unauthorized

