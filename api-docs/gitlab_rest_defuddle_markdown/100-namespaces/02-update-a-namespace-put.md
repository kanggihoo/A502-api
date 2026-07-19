# 02-Update a namespace [PUT]

`PUT /api/v4/namespaces/{id}`

Deprecated in 17.8

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Request Body (application/json)

```json
{
  "shared_runners_minutes_limit": integer, // Compute minutes quota for this namespace
  "extra_shared_runners_minutes_limit": integer, // Extra compute minutes for this namespace
  "additional_purchased_storage_size": integer, // Additional storage size for this namespace
  "additional_purchased_storage_ends_on": string, // End of subscription of the additional purchased storage
  "gitlab_subscription_attributes": {
    "start_date": string, // Start date of subscription
    "seats": integer, // Number of seats in subscription
    "max_seats_used": integer, // Highest number of active users in the last month
    "plan_code": string, // Subscription tier code
    "end_date": string, // End date of subscription
    "auto_renew": boolean, // Whether subscription will auto renew on end date
    "trial": boolean, // Whether the subscription is a trial
    "trial_ends_on": string, // End date of trial
    "trial_starts_on": string, // Start date of trial
    "trial_extension_type": integer, // Whether subscription is an extended or reactivated trial
  }, // Object that contains information on the GitLab subscription
}
```
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

#### 404 - Not Found

