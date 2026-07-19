# Workflow schemes

This resource represents workflow schemes. Use it to manage workflow schemes and the workflow scheme's workflows and issue types.

A workflow scheme maps issue types to workflows. A workflow scheme can be associated with one or more projects, which enables the projects to use the workflow-issue type mappings.

Active workflow schemes (workflow schemes that are used by projects) cannot be edited. When an active workflow scheme is edited, a draft copy of the scheme is created. The draft workflow scheme is then be edited and published (replacing the active scheme).

See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.

## Endpoints

- [01-Get all workflow schemes [GET]](./01-get-all-workflow-schemes-get.md)
- [02-Create workflow scheme [POST]](./02-create-workflow-scheme-post.md)
- [03-Switch workflow scheme for project [POST]](./03-switch-workflow-scheme-for-project-post.md)
- [04-Bulk get workflow schemes [POST]](./04-bulk-get-workflow-schemes-post.md)
- [05-Update workflow scheme [POST]](./05-update-workflow-scheme-post.md)
- [06-Get required status mappings for workflow scheme update [POST]](./06-get-required-status-mappings-for-workflow-scheme-update-post.md)
- [07-Get workflow scheme [GET]](./07-get-workflow-scheme-get.md)
- [08-Classic update workflow scheme [PUT]](./08-classic-update-workflow-scheme-put.md)
- [09-Delete workflow scheme [DELETE]](./09-delete-workflow-scheme-delete.md)
- [10-Get default workflow [GET]](./10-get-default-workflow-get.md)
- [11-Update default workflow [PUT]](./11-update-default-workflow-put.md)
- [12-Delete default workflow [DELETE]](./12-delete-default-workflow-delete.md)
- [13-Get workflow for issue type in workflow scheme [GET]](./13-get-workflow-for-issue-type-in-workflow-scheme-get.md)
- [14-Set workflow for issue type in workflow scheme [PUT]](./14-set-workflow-for-issue-type-in-workflow-scheme-put.md)
- [15-Delete workflow for issue type in workflow scheme [DELETE]](./15-delete-workflow-for-issue-type-in-workflow-scheme-delete.md)
- [16-Get issue types for workflows in workflow scheme [GET]](./16-get-issue-types-for-workflows-in-workflow-scheme-get.md)
- [17-Set issue types for workflow in workflow scheme [PUT]](./17-set-issue-types-for-workflow-in-workflow-scheme-put.md)
- [18-Delete issue types for workflow in workflow scheme [DELETE]](./18-delete-issue-types-for-workflow-in-workflow-scheme-delete.md)
- [19-Get projects which are using a given workflow scheme [GET]](./19-get-projects-which-are-using-a-given-workflow-scheme-get.md)
