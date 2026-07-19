# Issue notification schemes

This resource represents notification schemes, lists of events and the recipients who will receive notifications for those events. Use it to get details of a notification scheme and a list of notification schemes.

### About notification schemes ###

A notification scheme is a list of events and recipients who will receive notifications for those events. The list is contained within the `notificationSchemeEvents` object and contains pairs of `events` and `notifications`:

 *  `event` Identifies the type of event. The events can be [Jira system events](https://support.atlassian.com/jira-cloud-administration/docs/configure-notification-schemes/) (see the *Events* section) or [custom events](https://support.atlassian.com/jira-cloud-administration/docs/add-a-custom-event/).
 *  `notifications` Identifies the [recipients](https://confluence.atlassian.com/x/8YdKLg#Creatinganotificationscheme-recipientsRecipients) of notifications for each event. Recipients can be any of the following types:
    
     *  `CurrentAssignee`
     *  `Reporter`
     *  `CurrentUser`
     *  `ProjectLead`
     *  `ComponentLead`
     *  `User` (the `parameter` is the user key)
     *  `Group` (the `parameter` is the group name)
     *  `ProjectRole` (the `parameter` is the project role ID)
     *  `EmailAddress` *(deprecated)*
     *  `AllWatchers`
     *  `UserCustomField` (the `parameter` is the ID of the custom field)
     *  `GroupCustomField`(the `parameter` is the ID of the custom field)

## Endpoints

- [01-Get notification schemes paginated [GET]](./01-get-notification-schemes-paginated-get.md)
- [02-Create notification scheme [POST]](./02-create-notification-scheme-post.md)
- [03-Get projects using notification schemes paginated [GET]](./03-get-projects-using-notification-schemes-paginated-get.md)
- [04-Get notification scheme [GET]](./04-get-notification-scheme-get.md)
- [05-Update notification scheme [PUT]](./05-update-notification-scheme-put.md)
- [06-Add notifications to notification scheme [PUT]](./06-add-notifications-to-notification-scheme-put.md)
- [07-Delete notification scheme [DELETE]](./07-delete-notification-scheme-delete.md)
- [08-Remove notification from notification scheme [DELETE]](./08-remove-notification-from-notification-scheme-delete.md)
