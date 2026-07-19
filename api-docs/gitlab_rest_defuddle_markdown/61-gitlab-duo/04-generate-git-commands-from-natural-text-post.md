# 04-Generate Git commands from natural text [POST]

`POST /api/v4/ai/llm/git_command`

Generates Git commands from natural language input

### Request Body (application/json)

```json
{
  "prompt": string (required), // Prompt used to generate the Git commands
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

