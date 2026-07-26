# 10-Get AI bridge E2E test helper state [GET]

`GET /api/v4/system/e2e/ai_bridge`

Retrieve the current in-memory AI bridge test helper state used for end-to-end tests.
This endpoint is only available when `EnableTesting` is enabled. `EnableTesting` is intended only for isolated non-production environments and must never be enabled in production.
##### Permissions
Must have `manage_system` permission.


### Responses

#### 200 - AI bridge test helper state retrieved successfully

Schema (application/json):
```json
{
  "status": {
    "available": boolean, // Whether the mocked AI bridge should be reported as available
    "reason": string, // Optional reason code when the mocked AI bridge is unavailable
  },
  "agents": [
    {
      "id": string, // Unique identifier for the agent
      "displayName": string, // Human-readable name for the agent
      "username": string, // Username associated with the agent bot
      "service_id": string, // ID of the service providing this agent
      "service_type": string, // Type of the service (e.g., openai, anthropic)
    }
  ], // Current mocked agent list
  "services": [
    {
      "id": string, // Unique identifier for the LLM service
      "name": string, // Name of the LLM service
      "type": string, // Type of the service (e.g., openai, anthropic, azure)
    }
  ], // Current mocked service list
  "agent_completions": {}, // Remaining queued mocked completions keyed by bridge operation
  "feature_flags": {
    "enable_ai_plugin_bridge": boolean, // Override for the EnableAIPluginBridge feature flag in test mode
    "enable_ai_recaps": boolean, // Override for the EnableAIRecaps feature flag in test mode
  },
  "record_requests": boolean, // Whether bridge request recording is currently enabled
  "recorded_requests": [
    {
      "operation": string, // Explicit bridge operation key such as recap_summary or rewrite
      "client_operation": string, // Client-facing operation routed through the bridge client
      "operation_sub_type": string, // Optional subtype used to disambiguate bridge requests
      "session_user_id": string, // Session user ID used when invoking the bridge
      "user_id": string, // Optional effective user ID passed through the bridge request
      "channel_id": string, // Optional channel context passed through the bridge request
      "agent_id": string, // Agent ID targeted by the bridge completion request
      "service_id": string, // Service ID targeted by the bridge completion request
      "messages": [
        {
          "role": string, // Role associated with the message payload
          "message": string, // Message content sent through the AI bridge
          "file_ids": [
            string
          ], // Optional file IDs attached to the bridge message
        }
      ], // Bridge messages sent for the recorded request
      "json_output_format": {}, // Optional JSON schema requested for structured bridge output
    }
  ], // Recorded bridge requests captured while record_requests was enabled
}
```

#### 403 - 

#### 501 - 

