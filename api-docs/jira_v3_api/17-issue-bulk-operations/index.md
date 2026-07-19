# Issue bulk operations

This resource represents the issue bulk operations. Use it to move multiple issues from one project to another project or edit fields of multiple issues in one go.  


For additional clarity, we have created a page with further examples and answers to frequently asked questions related to these APIs. You can access it here: [Bulk operation APIs: additional examples and FAQ](https://developer.atlassian.com/cloud/jira/platform/bulk-operation-additional-examples-and-faqs/).

### Authentication ###

Access to the issue bulk operations requires authentication. For information on how to authenticate API requests, refer to the [Basic auth for REST APIs documentation](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/).

### Rate limiting ###

The bulk edit and move APIs are subject to the usual rate limiting infrastructure in Jira. For more information, refer to [Rate limiting](https://developer.atlassian.com/cloud/jira/platform/rate-limiting/). Additionally, at any given time, only 5 concurrent requests can be sent across all users.

## Endpoints

- [01-Bulk delete issues [POST]](./01-bulk-delete-issues-post.md)
- [02-Get bulk editable fields [GET]](./02-get-bulk-editable-fields-get.md)
- [03-Bulk edit issues [POST]](./03-bulk-edit-issues-post.md)
- [04-Bulk move issues [POST]](./04-bulk-move-issues-post.md)
- [05-Get available transitions [GET]](./05-get-available-transitions-get.md)
- [06-Bulk transition issue statuses [POST]](./06-bulk-transition-issue-statuses-post.md)
- [07-Bulk unwatch issues [POST]](./07-bulk-unwatch-issues-post.md)
- [08-Bulk watch issues [POST]](./08-bulk-watch-issues-post.md)
- [09-Get bulk issue operation progress [GET]](./09-get-bulk-issue-operation-progress-get.md)
