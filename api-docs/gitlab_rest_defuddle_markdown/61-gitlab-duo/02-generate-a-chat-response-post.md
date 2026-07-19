# 02-Generate a Chat response [POST]

`POST /api/v4/chat/completions`

Generates a response for a GitLab Duo Chat question.

### Request Body (application/json)

```json
{
  "content": string (required), // Prompt from user
  "resource_type": enum("issue" | "epic" | "group" | "project" | "merge_request" | "commit" | "build" | "work_item"), // Resource type
  "resource_id": any,
  "referer_url": string, // Referer URL
  "client_subscription_id": string, // Client Subscription ID
  "with_clean_history": boolean, // Indicates if we need to reset the history before and after the request
  "project_id": integer, // Project ID. Required if resource_type is a commit.
  "current_file": {
    "file_name": string, // The name of the current file
    "content_above_cursor": string, // The content above cursor
    "content_below_cursor": string, // The content below cursor
    "selected_text": string, // The content currently selected by the user
  }, // Object that contains information about the current file
  "additional_context": [
    {
      "category": enum("file" | "snippet" | "merge_request" | "issue" | "dependency" | "local_git" | "terminal" | "user_rule" | "repository" | "directory" | "agent_user_environment") (required), // Category of the additional context.
      "id": string (required), // ID of the additional context.
      "content": string (required), // Content of the additional context.
      "metadata": {}, // Metadata of the additional context.
    }
  ], // List of additional context to be passed for the chat
}
```
### Responses

#### 201 - Created

#### 400 - Bad Request

