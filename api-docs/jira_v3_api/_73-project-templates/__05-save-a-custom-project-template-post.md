# 05-Save a custom project template [POST]

`POST /rest/api/3/project-template/save-template`

Save custom template

This API endpoint allows you to save a customised template

***Note: Custom Templates are only supported for Jira Enterprise edition.***

### Request Body (application/json)

```json
{
  "templateDescription": string, // The description of the template
  "templateFromProjectRequest": {
    "projectId": integer, // The ID of the target project
    "templateGenerationOptions": {
      "enableScreenDelegatedAdminSupport": boolean, // Enable screen delegated admin support for the template. This means screen and associated schemes will be copied rather than referenced.
      "enableWorkflowDelegatedAdminSupport": boolean, // Enable workflow delegated admin support for the template. This means workflows and workflow schemes will be copied rather than referenced.
    },
    "templateType": enum("LIVE" | "SNAPSHOT"), // The type of the template: LIVE | SNAPSHOT
  },
  "templateName": string, // The name of the template
}
```
### Responses

#### 200 - 200 response

Schema (application/json):
```json
{
  "projectTemplateKey": {
    "key": string,
    "uuid": string,
  },
}
```

