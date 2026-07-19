# 04-List commands' autocomplete data [GET]

`GET /api/v4/teams/{team_id}/commands/autocomplete_suggestions`

List commands' autocomplete data for the team.
##### Permissions
`view_team` for the team.
__Minimum server version__: 5.24


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `team_id` | `string` | `path` | Yes | Team GUID |
| `user_input` | `string` | `query` | Yes | String inputted by the user. |

### Responses

#### 200 - Commands' autocomplete data retrieval successful

Schema (application/json):
```json
[
  {
    "Complete": string, // Completed suggestion
    "Suggestion": string, // Predicted text user might want to input
    "Hint": string, // Hint about suggested input
    "Description": string, // Description of the suggested command
    "IconData": string, // Base64 encoded svg image
  }
]
```

#### 400 - 

#### 401 - 

#### 403 - 

