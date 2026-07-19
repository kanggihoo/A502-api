# 01-Rollout namespaces to be indexed up to n% [PUT]

`PUT /api/v4/elasticsearch_indexed_namespaces/rollout`

This feature was introduced in GitLab 12.7.

**DEPRECATED**: This endpoint is deprecated and for GitLab.com use only.

This will only ever increase the number of indexed namespaces. Providing a value lower than the current rolled out percentage will have no effect.

This percentage is never persisted but is used to calculate the number of new namespaces to rollout.

If the same percentage is applied again at a later time, due to possible new namespaces being created during the period, some of them will also be indexed. Therefore you may expect that setting this to 10%, then waiting a month and setting to 10% again will trigger new namespaces to be added (i.e. 10% of the number of newly created namespaces in the last month within the given plan).


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

