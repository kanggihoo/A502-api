# 01-Get the policies which are applied to a user's teams [GET]

`GET /api/v4/users/{user_id}/data_retention/team_policies`

Gets the policies which are applied to the all of the teams to which a user belongs.

__Minimum server version__: 5.35

##### Permissions
Must be logged in as the user or have the `manage_system` permission.

##### License
Requires an E20 license.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `user_id` | `string` | `path` | Yes | The ID of the user. This can also be "me" which will point to the current user. |
| `page` | `integer` | `query` | No | The page to select. |
| `per_page` | `integer` | `query` | No | The number of policies per page. |

### Responses

#### 200 - Teams for retention policy successfully retrieved.

Schema (application/json):
```json
{
  "policies": [
    {
      "team_id": string, // The team ID.
      "post_duration": integer, // The number of days a message will be retained before being deleted by this policy.
    }
  ], // The list of team policies.
  "total_count": integer, // The total number of team policies.
}
```

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

