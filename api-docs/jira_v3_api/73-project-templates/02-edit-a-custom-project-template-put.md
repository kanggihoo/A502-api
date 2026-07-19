# 02-Edit a custom project template [PUT]

`PUT /rest/api/3/project-template/edit-template`

Edit custom template

This API endpoint allows you to edit an existing customised template.

***Note: Custom Templates are only supported for Jira Enterprise edition.***

### Request Body (application/json)

```json
{
  "templateDescription": string, // The description of the template
  "templateGenerationOptions": {
    "enableScreenDelegatedAdminSupport": boolean, // Enable screen delegated admin support for the template. This means screen and associated schemes will be copied rather than referenced.
    "enableWorkflowDelegatedAdminSupport": boolean, // Enable workflow delegated admin support for the template. This means workflows and workflow schemes will be copied rather than referenced.
  },
  "templateKey": string, // The unique identifier of the template
  "templateName": string, // The name of the template
}
```
### Responses

#### 200 - 200 response

Schema (application/json):
```json
any
```

