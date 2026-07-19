# 28-Rewrite a message using AI [POST]

`POST /api/v4/posts/rewrite`

Rewrite a message using AI based on the specified action. The message will be processed by an AI agent and returned in a rewritten form.
##### Permissions
Must be authenticated.
__Minimum server version__: 11.2


### Request Body (application/json)

```json
{
  "agent_id": string (required), // The ID of the AI agent to use for rewriting
  "message": string (required), // The message text to rewrite
  "action": enum("custom" | "shorten" | "elaborate" | "improve_writing" | "fix_spelling" | "simplify" | "summarize") (required), // The rewrite action to perform
  "custom_prompt": string, // Custom prompt for rewriting. Required when action is "custom", optional otherwise.
}
```
### Responses

#### 200 - Message rewritten successfully

Schema (application/json):
```json
{
  "rewritten_text": string, // The rewritten message text
}
```

#### 400 - 

#### 401 - 

#### 500 - Internal server error

Schema (application/json):
```json
{
  "status_code": integer,
  "id": string,
  "message": string,
  "request_id": string,
}
```

