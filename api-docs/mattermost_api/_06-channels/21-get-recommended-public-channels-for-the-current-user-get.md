# 21-Get recommended public channels for the current user [GET]

`GET /api/v4/teams/{team_id}/channels/recommended`

Return the public channels on a team that have a membership policy
assigned, where the requesting user's attributes match to the policy.

Membership policies on public channels are advisory: anyone can still join
these channels. This endpoint surfaces them as "Recommended channels"
for the requester.

Returns an empty list if the Enterprise Advanced license is not
active, if `AccessControlSettings.EnableAttributeBasedAccessControl`
is `false`, or if the user's attributes do not match any active
public-channel policy in the team.

__Minimum server version__: 11.8

##### Permissions
Must be authenticated and have `list_team_channels` on the team.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |

### Responses

#### 200 - Recommended channels retrieval successful

Schema (application/json):
```json
[
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
]
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 404 - 

