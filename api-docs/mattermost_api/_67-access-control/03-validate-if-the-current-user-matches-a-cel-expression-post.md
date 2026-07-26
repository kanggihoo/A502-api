# 03-Validate if the current user matches a CEL expression [POST]

`POST /api/v4/access_control_policies/cel/validate_requester`

Validates whether the current authenticated user matches the given CEL expression.
This is used to determine if a channel admin can test expressions they match.
##### Permissions
Must have `manage_system` permission OR be a channel admin for the specified channel (channelId required for channel admins).


### Request Body (application/json)

```json
{
  "expression": string (required), // The CEL expression to validate against the current user.
  "channelId": string, // The channel ID for channel-specific permission checks (required for channel admins).
}
```
### Responses

#### 200 - Validation result returned successfully.

Schema (application/json):
```json
{
  "requester_matches": boolean (required), // Whether the current user matches the expression.
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

