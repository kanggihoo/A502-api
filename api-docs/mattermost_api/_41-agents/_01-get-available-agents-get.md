# 01-Get available agents [GET]

`GET /api/v4/agents`

Retrieve all available agents from the plugin's bridge API. If a user ID is provided, only agents accessible to that user are returned.
##### Permissions
Must be authenticated.
__Minimum server version__: 11.2


### Responses

#### 200 - Agents retrieved successfully

Schema (application/json):
```json
{
  "agents": [
    {
      "id": string, // Unique identifier for the agent
      "displayName": string, // Human-readable name for the agent
      "username": string, // Username associated with the agent bot
      "service_id": string, // ID of the service providing this agent
      "service_type": string, // Type of the service (e.g., openai, anthropic)
    }
  ], // List of available agents
}
```

#### 401 - 

#### 500 - 

