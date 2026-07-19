# 13-Patch a channel [PUT]

`PUT /api/v4/channels/{channel_id}/patch`

Partially update a channel by providing only the fields you want to update. Omitted fields will not be updated. At least one of the allowed fields must be provided.
**Public and private channels:** Can update `name`, `display_name`, `purpose`, `header`, `group_constrained`, `autotranslation`, and `banner_info` (subject to permissions and channel type).
**Direct and group message channels:** Only `header` and (when not restricted by config) `autotranslation` can be updated; the caller must be a channel member. Updating `name`, `display_name`, or `purpose` is not allowed.
The default channel (e.g. Town Square) cannot have its `name` changed.
##### Permissions
- **Public channel:** For property updates (name, display_name, purpose, header, group_constrained), `manage_public_channel_properties` is required. For `autotranslation`, `manage_public_channel_auto_translation` is required. For `banner_info`, `manage_public_channel_banner` is required (Channel Banner feature and Enterprise license required). - **Private channel:** For property updates, `manage_private_channel_properties` is required. For `autotranslation`, `manage_private_channel_auto_translation` is required. For `banner_info`, `manage_private_channel_banner` is required (Channel Banner feature and Enterprise license required). - **Direct or group message channel:** Must be a member of the channel; only `header` and (when allowed) `autotranslation` can be updated.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `channel_id` | `string` | `path` | Yes | Channel ID |

### Request Body (application/json)

```json
{
  "name": string, // The unique handle for the channel, will be present in the channel URL. Cannot be updated for direct or group message channels. Cannot be changed for the default channel (e.g. Town Square).
  "display_name": string, // The non-unique UI name for the channel. Cannot be updated for direct or group message channels.
  "purpose": string, // A short description of the purpose of the channel. Cannot be updated for direct or group message channels.
  "header": string, // Markdown-formatted text to display in the header of the channel
  "group_constrained": boolean, // When true, only members of the linked LDAP groups can join the channel. Only applicable to public and private channels.
  "autotranslation": boolean, // Enable or disable automatic message translation in the channel. Requires the auto-translation feature and appropriate channel permission. May be restricted for direct and group message channels by server configuration.
  "banner_info": {
    "enabled": boolean, // enabled indicates whether the channel banner is enabled or not
    "text": string, // text is the actual text that renders in the channel banner. Markdown is supported.
    "background_color": string, // background_color is the HEX color code for the banner's background
  },
  "managed_category_name": string, // The name of the managed category to assign this channel to. Set to an empty string to clear. Requires an Enterprise license and the `ManagedChannelCategories` feature flag to be enabled.
  "default_category_name": string, // Default sidebar category name for members when joining this channel. Set to an empty string to clear. Requires `EnableChannelCategorySorting` to be enabled on the server.
}
```
### Responses

#### 200 - Channel patch successful

Schema (application/json):
```json
{
  "id": string,
  "create_at": integer, // The time in milliseconds a channel was created
  "update_at": integer, // The time in milliseconds a channel was last updated
  "delete_at": integer, // The time in milliseconds a channel was deleted
  "team_id": string,
  "type": string,
  "display_name": string,
  "name": string,
  "header": string,
  "purpose": string,
  "last_post_at": integer, // The time in milliseconds of the last post of a channel
  "total_msg_count": integer,
  "extra_update_at": integer, // Deprecated in Mattermost 5.0 release
  "creator_id": string,
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

