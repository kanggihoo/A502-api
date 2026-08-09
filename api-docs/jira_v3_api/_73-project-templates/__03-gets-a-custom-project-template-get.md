# 03-Gets a custom project template [GET]

`GET /rest/api/3/project-template/live-template`

Get custom template

This API endpoint allows you to get a live custom project template details by either templateKey or projectId

***Note: Custom Templates are only supported for Jira Enterprise edition.***

### Parameters

| Name | Type | In | Required | Description |
| --- | --- | --- | --- | --- |
| `projectId` | `string` | `query` | No | optional - The \{@link String\} containing the project key linked to the custom template to retrieve |
| `templateKey` | `string` | `query` | No | optional - The \{@link String\} containing the key of the custom template to retrieve |

### Responses

#### 200 - 200 response

Schema (application/json):
```json
{
  "archetype": {
    "realType": enum("BUSINESS" | "SOFTWARE" | "PRODUCT_DISCOVERY" | "SERVICE_DESK" | "CUSTOMER_SERVICE" | "OPS"),
    "style": enum("classic" | "next-gen"),
    "type": enum("BUSINESS" | "SOFTWARE" | "PRODUCT_DISCOVERY" | "SERVICE_DESK" | "CUSTOMER_SERVICE" | "OPS"),
  },
  "defaultBoardView": string,
  "description": string,
  "liveTemplateProjectIdReference": integer,
  "name": string,
  "projectTemplateKey": {
    "key": string,
    "uuid": string,
  },
  "snapshotTemplate": {},
  "templateGenerationOptions": {
    "enableScreenDelegatedAdminSupport": boolean, // Enable screen delegated admin support for the template. This means screen and associated schemes will be copied rather than referenced.
    "enableWorkflowDelegatedAdminSupport": boolean, // Enable workflow delegated admin support for the template. This means workflows and workflow schemes will be copied rather than referenced.
  },
  "type": enum("LIVE" | "SNAPSHOT"),
}
```

