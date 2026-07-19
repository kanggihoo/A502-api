# 04-Run manual testing helpers [GET]

`GET /manualtest`

Invokes manual test helpers used by developers and automated manual test scenarios.
This endpoint is only registered when `ServiceSettings.EnableTesting` is enabled.

##### Permissions

None. Authentication is not required; this route uses the same handler stack as other unauthenticated API handlers (`APIHandler`).

__Security note:__ Only enable `EnableTesting` on non-production, developer-oriented deployments.


### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `test` | `string` | `query` | Yes | Name of the manual test to run. |
| `uid` | `string` | `query` | No | Optional unique value used to randomize generated resources. |
| `username` | `string` | `query` | No | Optional username used for helper account creation. |
| `teamname` | `string` | `query` | No | Optional team display name used for helper team creation. |

### Responses

#### 307 - Manual test setup completed and redirected to the default channel.

#### 400 - 

#### 500 - 

