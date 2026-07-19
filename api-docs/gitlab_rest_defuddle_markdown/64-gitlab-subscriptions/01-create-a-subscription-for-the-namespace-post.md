# 01-Create a subscription for the namespace [POST]

`POST /api/v4/namespaces/{id}/gitlab_subscription`

Deprecated in GitLab 17.7

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `id` | `string` | `path` | Yes | The ID of a namespace |

### Request Body (application/json)

```json
{
  "start_date": string (required), // The date when subscription was started
  "end_date": string, // End date of subscription
  "plan_code": string, // Subscription tier code
  "seats": integer, // Number of seats in subscription
  "max_seats_used": integer, // Highest number of active users in the last month
  "auto_renew": boolean, // Whether subscription will auto renew on end date
  "trial": boolean, // Whether the subscription is a trial
  "trial_ends_on": string, // End date of trial
  "trial_starts_on": string, // Start date of trial
  "trial_extension_type": integer, // Whether the trial was extended or reactivated
}
```
### Responses

#### 201 - Created

Schema (application/json):
```json
{
  "plan": {},
  "usage": {},
  "billing": {},
}
```

#### 400 - Bad Request

#### 404 - Not Found

