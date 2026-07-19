# 02-Get agents bridge status [GET]

`GET /api/v4/agents/status`

Retrieve the status of the AI plugin bridge. Returns availability boolean and a reason code if unavailable.
##### Permissions
Must be authenticated.
__Minimum server version__: 11.2


### Responses

#### 200 - Status retrieved successfully

Schema (application/json):
```json
{
  "available": boolean, // Whether the AI plugin bridge is available
  "reason": string, // Reason code if not available (translation ID)
}
```

#### 401 - 

#### 500 - 

