# 170-Generate code completions [POST]

`POST /api/v4/code_suggestions/completions`

Generates code completions. Uses the AI abstraction layer to generate code completions. Requests to this endpoint are proxied to the AI Gateway.

### Request Body (application/json)

```json
{
  "current_file": {
    "file_name": string (required), // The name of the current file
    "content_above_cursor": string (required), // The content above cursor
    "content_below_cursor": string, // The content below cursor
  } (required), // Object that contains information about the current file
  "intent": enum("completion" | "generation"), // The intent of the completion request, current options are "completion" or "generation"
  "generation_type": enum("comment" | "empty_function" | "small_file"), // The type of generation request
  "stream": boolean, // The option to stream code completion response
  "project_path": string, // The path of the project
  "user_instruction": string, // Additional instructions provided by a user
  "context": [
    {
      "type": enum("file" | "snippet") (required), // The type of a related part of context
      "name": string (required), // The name of a related part of context
      "content": string (required), // The content of a part of context
    }
  ], // List of related context parts
}
```
### Responses

#### 200 - OK

#### 400 - Bad Request

