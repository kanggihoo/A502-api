# 01-Create custom project [POST]

`POST /rest/api/3/project-template`

Creates a project based on a custom template provided in the request.

The request body should contain the project details and the capabilities that comprise the project:

 *  `details` \- represents the project details settings
 *  `template` \- represents a list of capabilities responsible for creating specific parts of a project

A capability is defined as a unit of configuration for the project you want to create.

This operation is:

 *  [asynchronous](#async). Follow the `Location` link in the response header to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

***Note: This API is only supported for Jira Enterprise edition.***

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Request Body (application/json)

```json
{
  "details": {
    "accessLevel": enum("open" | "limited" | "private" | "free"), // The access level of the project. Only used by team-managed project
    "additionalProperties": {}, // Additional properties of the project
    "assigneeType": enum("PROJECT_DEFAULT" | "COMPONENT_LEAD" | "PROJECT_LEAD" | "UNASSIGNED"), // The default assignee when creating issues in the project
    "avatarId": integer, // The ID of the project's avatar. Use the \[Get project avatars\](\#api-rest-api-3-project-projectIdOrKey-avatar-get) operation to list the available avatars in a project.
    "categoryId": integer, // The ID of the project's category. A complete list of category IDs is found using the [Get all project categories](#api-rest-api-3-projectCategory-get) operation.
    "description": string, // Brief description of the project
    "enableComponents": boolean, // Whether components are enabled for the project. Only used by company-managed project
    "key": string, // Project keys must be unique and start with an uppercase letter followed by one or more uppercase alphanumeric characters. The maximum length is 10 characters.
    "language": string, // The default language for the project
    "leadAccountId": string, // The account ID of the project lead. Either `lead` or `leadAccountId` must be set when creating a project. Cannot be provided with `lead`.
    "name": string, // Name of the project
    "url": string, // A link to information about this project, such as project documentation
  },
  "template": {
    "boardFeatures": {
      "boardFeatures": {}, // A map of board PCRIs to the list of features to enable on each board.
    },
    "boards": {
      "boards": [
        {
          "boardFilterJQL": string, // Takes in a JQL string to create a new filter. If no value is provided, it'll default to a JQL filter for the project creating
          "cardColorStrategy": enum("ISSUE_TYPE" | "REQUEST_TYPE" | "ASSIGNEE" | "PRIORITY" | "NONE" | "CUSTOM"), // Card color settings of the board
          "cardLayout": {
            "showDaysInColumn": enum(true | false), // Whether to show days in column
          },
          "cardLayouts": [
            {
              "fieldId": string,
              "id": integer,
              "mode": enum("PLAN" | "WORK"),
              "position": integer,
            }
          ], // Card layout settings of the board
          "columns": [
            {
              "maximumIssueConstraint": integer, // The maximum issue constraint for the column
              "minimumIssueConstraint": integer, // The minimum issue constraint for the column
              "name": string, // The name of the column
              "statusIds": [
                {
                  "anID": boolean,
                  "areference": boolean,
                  "entityId": string,
                  "entityType": string,
                  "id": string,
                  "type": enum("id" | "ref"),
                }
              ], // The status IDs for the column
            }
          ], // The columns of the board
          "features": [
            {
              "featureKey": enum("ESTIMATION" | "SPRINTS"), // The key of the feature
              "state": enum(true | false), // Whether the feature should be turned on or off
            }
          ], // Feature settings for the board. Deprecated: use boardFeatures capability instead.
          "name": string, // The name of the board
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "quickFilters": [
            {
              "description": string, // The description of the quick filter
              "jqlQuery": string, // The jql query for the quick filter
              "name": string, // The name of the quick filter
            }
          ], // The quick filters for the board.
          "supportsSprint": boolean, // Whether sprints are supported on the board
          "swimlanes": {
            "customSwimlanes": [
              {
                "description": string, // The description of the quick filter
                "jqlQuery": string, // The jql query for the quick filter
                "name": string, // The name of the quick filter
              }
            ], // The custom swimlane definitions.
            "defaultCustomSwimlaneName": string, // The name of the custom swimlane to use for work items that don't match any other swimlanes.
            "swimlaneStrategy": enum("none" | "custom" | "parentChild" | "assignee" | "assigneeUnassignedFirst" | "epic" | "project" | "issueparent" | "issuechildren" | "request_type"), // The swimlane strategy for the board.
          },
          "workingDaysConfig": {
            "friday": boolean,
            "id": integer,
            "monday": boolean,
            "nonWorkingDays": [
              {
                "id": integer,
                "iso8601Date": string,
              }
            ],
            "saturday": boolean,
            "sunday": boolean,
            "thursday": boolean,
            "timezoneId": string,
            "tuesday": boolean,
            "wednesday": boolean,
          },
        }
      ], // The boards to be associated with the project.
    },
    "field": {
      "customFieldDefinitions": [
        {
          "cfType": string, // The type of the custom field
          "description": string, // The description of the custom field
          "name": string, // The name of the custom field
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use when there is a conflict with an existing custom field. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "scope": enum("GLOBAL" | "TEMPLATE" | "PROJECT"), // Allows an overwrite to declare the new Custom Field to be created as a GLOBAL-scoped field. Leave this as empty or null to use the project's default scope.
          "searcherKey": string, // The searcher key of the custom field
        }
      ], // The custom field definitions. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-fields/\#api-rest-api-3-field-post
      "fieldLayoutScheme": {
        "defaultFieldLayout": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
        "description": string, // The description of the field layout scheme
        "explicitMappings": {}, // There is a default configuration "fieldlayout" that is applied to all issue types using this scheme that don't have an explicit mapping users can create (or re-use existing) configurations for other issue types and map them to this scheme
        "name": string, // The name of the field layout scheme
        "pcri": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
      },
      "fieldLayouts": [
        {
          "configuration": [
            {
              "field": boolean, // Whether to show the field
              "pcri": {
                "anID": boolean,
                "areference": boolean,
                "entityId": string,
                "entityType": string,
                "id": string,
                "type": enum("id" | "ref"),
              },
              "required": boolean, // Whether the field is required
            }
          ], // The field layout configuration. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/\#api-rest-api-3-fieldconfiguration-post
          "description": string, // The description of the field layout
          "name": string, // The name of the field layout
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
        }
      ], // The field layouts configuration.
      "fieldScheme": {
        "description": string, // The description of the field scheme
        "items": [
          {
            "description": string, // The description of the field association item
            "pcri": {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            },
            "qualifierId": {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            },
            "qualifierType": {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            },
            "rendererType": string, // The renderer type of the field
            "required": boolean, // Whether the field is required
          }
        ], // The field association items for this field scheme.
        "name": string, // The name of the field scheme
        "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use when there is a conflict with an existing field scheme. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
        "pcri": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
      },
      "issueLayouts": [
        {
          "containerId": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "issueLayoutType": enum("ISSUE_VIEW" | "ISSUE_CREATE" | "REQUEST_FORM"), // The issue layout type
          "items": [
            {
              "itemKey": {
                "anID": boolean,
                "areference": boolean,
                "entityId": string,
                "entityType": string,
                "id": string,
                "type": enum("id" | "ref"),
              },
              "properties": {}, // Additional properties for this item. This field is only used when the type is FIELD.
              "sectionType": enum("content" | "primaryContext" | "secondaryContext"), // The item section type
              "type": enum("FIELD"), // The item type. Currently only support FIELD
            }
          ], // The configuration of items in the issue layout
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
        }
      ], // The issue layouts configuration
      "issueTypeScreenScheme": {
        "defaultScreenScheme": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
        "description": string, // The description of the issue type screen scheme
        "explicitMappings": {}, // The IDs of the screen schemes for the issue type IDs and default. A default entry is required to create an issue type screen scheme, it defines the mapping for all issue types without a screen scheme.
        "name": string, // The name of the issue type screen scheme
        "pcri": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
      },
      "screenScheme": [
        {
          "defaultScreen": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "description": string, // The description of the screen scheme
          "name": string, // The name of the screen scheme
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "screens": {}, // Similar to the field layout scheme those mappings allow users to set different screens for different operations: default - always there, applied to all operations that don't have an explicit mapping `create`, `view`, `edit` - specific operations that are available and users can assign a different screen for each one of them https://support.atlassian.com/jira-cloud-administration/docs/manage-screen-schemes/\#Associating-a-screen-with-an-issue-operation
        }
      ], // The screen schemes See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-schemes/\#api-rest-api-3-screenscheme-post
      "screens": [
        {
          "description": string, // The description of the screen
          "name": string, // The name of the screen
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "tabs": [
            {
              "fields": [
                {
                  "anID": boolean,
                  "areference": boolean,
                  "entityId": string,
                  "entityType": string,
                  "id": string,
                  "type": enum("id" | "ref"),
                }
              ], // The list of resource identifier of the field associated to the tab. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/\#api-rest-api-3-screens-screenid-tabs-tabid-fields-post
              "name": string, // The name of the tab
            }
          ], // The tabs of the screen. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screen-tab-fields/\#api-rest-api-3-screens-screenid-tabs-tabid-fields-post
        }
      ], // The screens. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-screens/\#api-rest-api-3-screens-post
    },
    "issueType": {
      "issueTypeHierarchy": [
        {
          "hierarchyLevel": integer, // The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks
          "name": string, // The name of the issue type
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
        }
      ], // Defines the issue type hierarhy to be created and used during this project creation. This will only add new levels if there isn't an existing level
      "issueTypeScheme": {
        "defaultIssueTypeId": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
        "description": string, // The description of the issue type scheme
        "issueTypeIds": [
          {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          }
        ], // The issue type IDs for the issue type scheme
        "name": string, // The name of the issue type scheme
        "pcri": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
      },
      "issueTypes": [
        {
          "avatarId": integer, // The avatar ID of the issue type. Go to https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-avatars/\#api-rest-api-3-avatar-type-system-get to choose an avatarId existing in Jira
          "description": string, // The description of the issue type
          "hierarchyLevel": integer, // The hierarchy level of the issue type. 0, 1, 2, 3 .. n; Negative values for subtasks
          "name": string, // The name of the issue type
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The conflict strategy to use when the issue type already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
        }
      ], // Only needed if you want to create issue types, you can otherwise use the ids of issue types in the scheme configuration
    },
    "notification": {
      "description": string, // The description of the notification scheme
      "name": string, // The name of the notification scheme
      "notificationSchemeEvents": [
        {
          "event": {
            "id": string, // The event ID to use for reference in the payload
          },
          "notifications": [
            {
              "notificationType": string, // The type of notification.
              "parameter": string, // The parameter of the notification, should be eiither null if not required, or PCRI.
            }
          ], // The configuration for notification recipents
        }
      ], // The events and notifications for the notification scheme
      "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use when there is a conflict with an existing entity
      "pcri": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
    },
    "permissionScheme": {
      "addAddonRole": boolean, // Configuration to generate addon role. Default is false if null. Only applies to GLOBAL-scoped permission scheme
      "description": string, // The description of the permission scheme
      "grants": [
        {
          "applicationAccess": [
            string
          ],
          "groupCustomFields": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ],
          "groups": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ],
          "permissionKeys": [
            string
          ],
          "projectRoles": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ],
          "specialGrants": [
            string
          ],
          "userCustomFields": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ],
          "users": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ],
        }
      ], // List of permission grants
      "name": string, // The name of the permission scheme
      "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use when there is a conflict with an existing permission scheme. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - If the entity exist, try and create a new one with a different name
      "pcri": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
    },
    "project": {
      "fieldLayoutSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "issueSecuritySchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "issueTypeSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "issueTypeScreenSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "notificationSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "pcri": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "permissionSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "projectTypeKey": enum("software" | "business" | "service_desk" | "product_discovery"), // The [project type](https://confluence.atlassian.com/x/GwiiLQ#Jiraapplicationsoverview-Productfeaturesandprojecttypes), which defines the application-specific feature set. If you don't specify the project template you have to specify the project type.
      "workflowSchemeId": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
    },
    "role": {
      "roleToProjectActors": {}, // A map of role PCRI (can be ID or REF) to a list of user or group PCRI IDs to associate with the role and project.
      "roles": [
        {
          "defaultActors": [
            {
              "anID": boolean,
              "areference": boolean,
              "entityId": string,
              "entityType": string,
              "id": string,
              "type": enum("id" | "ref"),
            }
          ], // The default actors for the role. By adding default actors, the role will be added to any future projects created
          "description": string, // The description of the role
          "name": string, // The name of the role
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use when there is a conflict with an existing project role. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "type": enum("HIDDEN" | "VIEWABLE" | "AI_AGENT" | "EDITABLE" | "GUEST"), // The type of the role. Only used by project-scoped project
        }
      ], // The list of roles to create.
    },
    "scope": {
      "type": enum("GLOBAL" | "PROJECT"), // The type of the scope. Use `GLOBAL` or empty for company-managed project, and `PROJECT` for team-managed project
    },
    "security": {
      "description": string, // The description of the security scheme
      "name": string, // The name of the security scheme
      "pcri": {
        "anID": boolean,
        "areference": boolean,
        "entityId": string,
        "entityType": string,
        "id": string,
        "type": enum("id" | "ref"),
      },
      "securityLevels": [
        {
          "description": string, // The description of the security level
          "isDefault": enum(true | false), // Whether the security level is default for the security scheme
          "name": string, // The name of the security level
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "securityLevelMembers": [
            {
              "parameter": string, // Defines the value associated with the type. For reporter this would be \{"null"\}; for users this would be the names of specific users); for group this would be group names like \{"administrators", "jira-administrators", "jira-users"\}
              "type": enum("group" | "reporter" | "users"), // The type of the security level member
            }
          ], // The members of the security level
        }
      ], // The security levels for the security scheme
    },
    "workflow": {
      "statuses": [
        {
          "description": string, // The description of the status
          "name": string, // The name of the status
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The conflict strategy for the status already exists. FAIL - Fail execution, this always needs to be unique; USE - Use the existing entity and ignore new entity parameters; NEW - Create a new entity
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "statusCategory": enum("TODO" | "IN_PROGRESS" | "DONE"), // The status category of the status. The value is case-sensitive.
        }
      ], // The statuses for the workflow
      "workflowScheme": {
        "defaultWorkflow": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
        "description": string, // The description of the workflow scheme
        "explicitMappings": {}, // Association between issuetypes and workflows
        "name": string, // The name of the workflow scheme
        "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use if there is a conflict with another workflow scheme
        "pcri": {
          "anID": boolean,
          "areference": boolean,
          "entityId": string,
          "entityType": string,
          "id": string,
          "type": enum("id" | "ref"),
        },
      },
      "workflows": [
        {
          "description": string, // The description of the workflow
          "loopedTransitionContainerLayout": {
            "x": number, // The x coordinate of the status.
            "y": number, // The y coordinate of the status.
          },
          "name": string, // The name of the workflow
          "onConflict": enum("FAIL" | "USE" | "NEW"), // The strategy to use if there is a conflict with another workflow
          "pcri": {
            "anID": boolean,
            "areference": boolean,
            "entityId": string,
            "entityType": string,
            "id": string,
            "type": enum("id" | "ref"),
          },
          "startPointLayout": {
            "x": number, // The x coordinate of the status.
            "y": number, // The y coordinate of the status.
          },
          "statuses": [
            {
              "layout": {
                "x": number, // The x coordinate of the status.
                "y": number, // The y coordinate of the status.
              },
              "pcri": {
                "anID": boolean,
                "areference": boolean,
                "entityId": string,
                "entityType": string,
                "id": string,
                "type": enum("id" | "ref"),
              },
              "properties": {}, // The properties of the workflow status.
            }
          ], // The statuses to be used in the workflow
          "transitions": [
            {
              "actions": [
                {
                  "parameters": {}, // The parameters of the rule
                  "ruleKey": string, // The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\#api-rest-api-3-workflows-capabilities-get
                }
              ], // The actions that are performed when the transition is made
              "conditions": {
                "conditionGroup": [
                  Ref(ConditionGroupPayload) [recursive]
                ], // The nested conditions of the condition group.
                "conditions": [
                  {
                    "parameters": {}, // The parameters of the rule
                    "ruleKey": string, // The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\#api-rest-api-3-workflows-capabilities-get
                  }
                ], // The rules for this condition.
                "operation": enum("ANY" | "ALL"), // Determines how the conditions in the group are evaluated. Accepts either `ANY` or `ALL`. If `ANY` is used, at least one condition in the group must be true for the group to evaluate to true. If `ALL` is used, all conditions in the group must be true for the group to evaluate to true.
              },
              "customIssueEventId": string, // Mechanism in Jira for triggering certain actions, like notifications, automations, etc. Unless a custom notification scheme is configure, it's better not to provide any value here
              "description": string, // The description of the transition
              "from": [
                {
                  "fromPort": integer, // The port that the transition can be made from
                  "status": {
                    "anID": boolean,
                    "areference": boolean,
                    "entityId": string,
                    "entityType": string,
                    "id": string,
                    "type": enum("id" | "ref"),
                  },
                  "toPortOverride": integer, // The port that the transition goes to
                }
              ], // The statuses that the transition can be made from
              "id": integer, // The id of the transition
              "name": string, // The name of the transition
              "properties": {}, // The properties of the transition
              "to": {
                "port": integer, // Defines where the transition line will be connected to a status. Port 0 to 7 are acceptable values.
                "status": {
                  "anID": boolean,
                  "areference": boolean,
                  "entityId": string,
                  "entityType": string,
                  "id": string,
                  "type": enum("id" | "ref"),
                },
              },
              "transitionScreen": {
                "parameters": {}, // The parameters of the rule
                "ruleKey": string, // The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\#api-rest-api-3-workflows-capabilities-get
              },
              "triggers": [
                {
                  "parameters": {}, // The parameters of the rule
                  "ruleKey": string, // The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\#api-rest-api-3-workflows-capabilities-get
                }
              ], // The triggers that are performed when the transition is made
              "type": enum("global" | "initial" | "directed"), // The type of the transition
              "validators": [
                {
                  "parameters": {}, // The parameters of the rule
                  "ruleKey": string, // The key of the rule. See https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflows/\#api-rest-api-3-workflows-capabilities-get
                }
              ], // The validators that are performed when the transition is made
            }
          ], // The transitions for the workflow
        }
      ], // The transitions for the workflow
    },
  },
}
```
### Responses

#### 303 - The project creation task has been queued for execution

Schema (application/json):
```json
any
```

