# 04-Create workflow persistence (agent-initiated, limited privileges) [POST]

`POST /api/v4/ai/duo_workflows/agent_workflows`

Accessible via ai_workflows scope token. Does not accept agent_privileges or pre_approved_agent_privileges.

### Request Body (application/json)

```json
{
  "project_id": string, // The ID or path of the workflow project
  "namespace_id": string, // The ID or path of the workflow namespace
  "ai_catalog_item_consumer_id": integer, // The ID of AI Catalog ItemConsumer that configures which catalog item to execute.
  "start_workflow": boolean, // Optional parameter to start workflow in a CI pipeline.This feature is currently in an experimental state.
  "goal": string, // Goal of the workflow
  "workflow_definition": string, // workflow type based on its capability
  "allow_agent_to_request_user": boolean, // When this is enabled Duo Agent Platform may stop to ask the user questions before proceeding. When it is disabled Duo Agent Platform will always just run through the workflow without ever asking for user input. Defaults to true.
  "image": string, // Container image to use for running the workflow in CI pipeline.
  "source_branch": string, // Source branch for the CI pipeline. Uses default branch when not specified.
  "environment": enum("ide" | "web" | "chat_partial" | "chat" | "ambient"), // Environment for the workflow.
  "ai_catalog_item_version_id": integer, // The ID of AI Catalog ItemVersion that sourced flow config used by the workflow.
  "additional_context": [
    {
      "Category": string (required), // The category of the context detail
      "Content": string (required), // The content type of the context detail
    }
  ], // Additional Context required by the Flow, in JSON format. Contains an array of context details, where each detail is a Hash with a minimum of "Category" and "Content" keys.
  "shallow_clone": boolean, // Whether or not the workflow should use a shallow clone of the repository during its execution.  Defaults to true.
  "issue_id": integer, // IID of the Issue noteable that the workflow is associated with.
  "merge_request_id": integer, // IID of the MergeRequest noteable that the workflow is associated with.
}
```
### Responses

#### 201 - Created

#### 400 - Validation failed

#### 401 - Unauthorized

#### 403 - 403 Forbidden

#### 404 - Not found

