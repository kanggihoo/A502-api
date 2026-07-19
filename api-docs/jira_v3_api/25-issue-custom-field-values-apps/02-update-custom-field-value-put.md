# 02-Update custom field value [PUT]

`PUT /rest/api/3/app/field/{fieldIdOrKey}/value`

Updates the value of a custom field on one or more issues.

Apps can only perform this operation on [custom fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/) and [custom field types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) declared in their own manifests.

**[Permissions](#permissions) required:** Only the app that owns the custom field or custom field type can update its values with this operation.

The new `write:app-data:jira` OAuth scope is 100% optional now, and not using it won't break your app. However, we recommend adding it to your app's scope list because we will eventually make it mandatory.

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `fieldIdOrKey` | `string` | `path` | Yes | The ID or key of the custom field. For example, `customfield_10010`. |
| `generateChangelog` | `boolean` | `query` | No | Whether to generate a changelog for this update. |
| `generateAppEvents` | `boolean` | `query` | No | Whether to generate app events for this update. Suppresses Forge, Connect, OAuth 2.0, and admin-configured webhooks (registered via the Jira admin UI). Note: Suppressing events means that "issue updated" events will not be emitted for your app or any other apps installed in Jira. This may cause other apps to retain stale data for the updated field, resulting in potentially confusing behaviour. We do not recommend using this flag in a Marketplace app as it may result in incompatibilities with other apps that depend on up-to-date issue data. |

### Request Body (application/json)

```json
{
  "updates": [
    {
      "issueIds": [
        integer
      ] (required), // The list of issue IDs.
      "value": any (required), // The value for the custom field. The value must be compatible with the [custom field type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#data-types) as follows:   *  `string` the value must be a string.  *  `number` the value must be a number.  *  `datetime` the value must be a string that represents a date in the ISO format or the simplified extended ISO format. For example, `"2023-01-18T12:00:00-03:00"` or `"2023-01-18T12:00:00.000Z"`. However, the milliseconds part is ignored.  *  `user` the value must be an object that contains the `accountId` field.  *  `group` the value must be an object that contains the group `name` or `groupId` field. Because group names can change, we recommend using `groupId`.  A list of appropriate values must be provided if the field is of the `list` [collection type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#collection-types).
    }
  ], // The list of custom field update details.
}
```
### Responses

#### 204 - Returned if the request is successful.

Schema (application/json):
```json
any
```

#### 400 - Returned if the request is invalid.

#### 403 - Returned if the request is not authenticated as the app that provided the field.

#### 404 - Returned if the field is not found.

