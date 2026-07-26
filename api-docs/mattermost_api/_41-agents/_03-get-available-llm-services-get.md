# 03-Get available LLM services [GET]

`GET /api/v4/llmservices`

Retrieve all available LLM services from the plugin's bridge API. If a user ID is provided, only services accessible to that user (via their permitted bots) are returned.
##### Permissions
Must be authenticated.
__Minimum server version__: 11.2


### Responses

#### 200 - LLM services retrieved successfully

Schema (application/json):
```json
{
  "services": [
    {
      "id": string, // Unique identifier for the LLM service
      "name": string, // Name of the LLM service
      "type": string, // Type of the service (e.g., openai, anthropic, azure)
    }
  ], // List of available LLM services
}
```

#### 401 - 

#### 500 - 

