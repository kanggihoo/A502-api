# 05-Simulate an access control policy decision for an explicit user list [POST]

`POST /api/v4/access_control_policies/cel/simulate_users`

Runs the dual-lane PDP simulation against a draft (unsaved) access
control policy for an explicit set of users (with optional per-user
session-attribute overrides). The server compiles the draft
in-memory, layers on persisted higher-scoped permission policies,
and returns per-user, per-action ALLOW/DENY decisions plus blame
attribution for any deny.

Backs the picker-driven "Simulate access" UX in the System Console
and Channel Settings so authors can see how a draft interacts with
persisted higher-scoped policies before saving.

Gated by the `PermissionPolicies` feature flag and the Enterprise
Advanced license. Returns 501 (Not Implemented) when either is
missing.

##### Permissions
Must have the `manage_system` permission, OR be a team admin with
`manage_team_access_rules` on the request's `team_id` (when any
provided `channel_id` resolves to a channel in that team), OR be a
channel admin with `manage_channel_access_rules` on the request's
`channel_id`.


### Request Body (application/json)

```json
{
  "policy": {
    "id": string, // The unique identifier of the policy.
    "name": string, // The unique name for the policy.
    "display_name": string, // The human-readable name for the policy.
    "description": string, // A description of the policy.
    "expression": string, // The CEL expression defining the policy rules.
    "is_active": boolean, // Whether the policy is currently active and enforced.
    "create_at": integer, // The time in milliseconds the policy was created.
    "update_at": integer, // The time in milliseconds the policy was last updated.
    "delete_at": integer, // The time in milliseconds the policy was deleted.
  } (required),
  "actions": [
    string
  ] (required), // Permission actions to simulate (e.g. `upload_file_attachment`, `download_file_attachment`). At least one action is required — the picker UX only makes sense once an action is in scope. The backend rejects empty arrays with `app.pap.simulate.missing_actions` (HTTP 400); `minItems` lets OpenAPI tooling catch that earlier on the client. 
  "rule_name": string, // Identifies which rule in `policy.rules` the author is editing (used for blame attribution). When set, denies originating from this rule are tagged `source=this_rule`; other denies in the same draft are tagged `source=sibling_rule`. 
  "channel_id": string, // Provides resource context for delegated channel admins and for resource-lane evaluation when `policy.type == "channel"`. 
  "team_id": string, // Provides team context for team-level delegated admins.
  "users": [
    {
      "user_id": string (required), // ID of the user to evaluate the draft policy against.
      "use_active_session": boolean, // When true, inject the requesting admin's `session.*` attributes (network_status, device_managed, ip_range, etc.) into this user's evaluation context. Forward-compatible with future PDP work that populates session attributes on the request context. 
      "session_overrides": {}, // Replaces individual `session.*` attributes for this user only. Applied on top of the active-session snapshot when both are set, so a "configure session" panel can shadow specific values without discarding the rest of the active session. 
    }
  ] (required), // Explicit user list to evaluate, with per-user session-attribute overrides. At least one user is required (the backend rejects empty arrays with `app.pap.simulate.missing_users`). 
  "evaluation_scope": enum("all" | "this_rule"), // Selects whether the simulator considers only the rule under simulation (`this_rule`) or co-evaluates every contributing program (`all`). Empty defaults to `this_rule` on the server. `this_rule` is the authoring-time "what does this rule alone do?" view: useful for iterating on a single rule without sibling rules shadowing or compensating for it. `all` mirrors the live PDP at request time. 
}
```
### Responses

#### 200 - Per-user, per-action simulation results.

Schema (application/json):
```json
{
  "results": [
    {
      "user": {
        "id": string,
        "create_at": integer, // The time in milliseconds a user was created
        "update_at": integer, // The time in milliseconds a user was last updated
        "delete_at": integer, // The time in milliseconds a user was deleted
        "username": string,
        "first_name": string,
        "last_name": string,
        "nickname": string,
        "email": string,
        "email_verified": boolean,
        "auth_service": string,
        "roles": string,
        "locale": string,
        "notify_props": {
          "email": string, // Set to "true" to enable email notifications, "false" to disable. Defaults to "true".
          "push": string, // Set to "all" to receive push notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "mention".
          "desktop": string, // Set to "all" to receive desktop notifications for all activity, "mention" for mentions and direct messages only, and "none" to disable. Defaults to "all".
          "desktop_sound": string, // Set to "true" to enable sound on desktop notifications, "false" to disable. Defaults to "true".
          "mention_keys": string, // A comma-separated list of words to count as mentions. Defaults to username and @username.
          "channel": string, // Set to "true" to enable channel-wide notifications (@channel, @all, etc.), "false" to disable. Defaults to "true".
          "first_name": string, // Set to "true" to enable mentions for first name. Defaults to "true" if a first name is set, "false" otherwise.
          "auto_responder_message": string, // The message sent to users when they are auto-responded to. Defaults to "".
          "push_threads": string, // Set to "all" to enable mobile push notifications for followed threads and "none" to disable. Defaults to "all".
          "comments": string, // Set to "any" to enable notifications for comments to any post you have replied to, "root" for comments on your posts, and "never" to disable. Only affects users with collapsed reply threads disabled. Defaults to "never".
          "desktop_threads": string, // Set to "all" to enable desktop notifications for followed threads and "none" to disable. Defaults to "all".
          "email_threads": string, // Set to "all" to enable email notifications for followed threads and "none" to disable. Defaults to "all".
        },
        "props": {},
        "last_password_update": integer,
        "last_picture_update": integer,
        "failed_attempts": integer,
        "mfa_active": boolean,
        "timezone": {
          "useAutomaticTimezone": string, // Set to "true" to use the browser/system timezone, "false" to set manually. Defaults to "true".
          "manualTimezone": string, // Value when setting manually the timezone, i.e. "Europe/Berlin".
          "automaticTimezone": string, // This value is set automatically when the "useAutomaticTimezone" is set to "true".
        },
        "terms_of_service_id": string, // ID of accepted terms of service, if any. This field is not present if empty.
        "terms_of_service_create_at": integer, // The time in milliseconds the user accepted the terms of service
      },
      "decisions": {}, // Per-action verdicts for the user. When `sessions` is populated this represents the "headline" decision (e.g. from the most-recently-active session) so the picker can render a single chip without consulting `sessions`. 
      "sessions": [
        {
          "device": string,
          "network": string,
          "last_active_at": integer, // Last-active timestamp in milliseconds since epoch.
          "decisions": {}, // Per-action verdicts for this specific session.
          "attributes": {}, // Session-attribute snapshot used when evaluating this session (network_status, device_managed, ip_range, etc.). Surfaced in the per-row "Decision details" view. 
        }
      ], // Optional per-session breakdown. When populated the picker renders a Recent activity expand row revealing one decision chip per session. Empty/undefined falls back to a single user-level chip. 
      "attributes": {}, // User profile attribute snapshot used when evaluating this user (department, region, clearance, etc.). 
    }
  ],
  "total": integer, // Total number of users evaluated (matches `results.length` for the picker endpoint since the caller supplies the user list explicitly). 
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

#### 501 - 

