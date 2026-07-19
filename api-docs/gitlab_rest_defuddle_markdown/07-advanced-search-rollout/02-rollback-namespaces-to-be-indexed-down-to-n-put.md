# 02-Rollback namespaces to be indexed down to n% [PUT]

`PUT /api/v4/elasticsearch_indexed_namespaces/rollback`

This feature was introduced in GitLab 12.7.

**DEPRECATED**: This endpoint is deprecated and for GitLab.com use only.

This will only ever decrease the number of indexed namespaces. Providing a value higher than the current rolled out percentage will have no effect.

This percentage is never persisted but is used to calculate the number of namespaces to rollback.


### Request Body (application/json)

```json
{
  "percentage": integer (required), // Percentage of namespaces to rollout Elasticsearch for
  "plan": enum("bronze" | "silver" | "premium" | "gold" | "ultimate" | "ultimate_trial" | "ultimate_trial_paid_customer" | "premium_trial" | "opensource") (required), // Subscription tier to rollout Elasticsearch for
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

