# 03-Retrieve namespace details [GET]

`GET /api/v4/namespaces/{id}`

Retrieves a specified namespace.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `any` | `path` | Yes | ID or URL-encoded path of the namespace |

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

#### 404 - Not found

