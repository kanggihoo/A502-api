# Merge request approvals

  ### 4. Merge request approvals API

  • 유용성: P1 (유용 - MR 승인 상태 및 승인 작업).
      • Retrieve approval state (10번): MR 승인 상태(승인 완료 여부)를 대시보드에 표시.
      • Approve / Unapprove MR (12, 13번): 대시보드/알림에서 즉시 MR 승인 처리.
      • Approval rules (01~09번): 고급 그룹/프로젝트 승인 규칙 설정은 GitLab Premium/Ultimate (유료
      티어) 제약 가능성 높음.
Operations related to merge request approvals.

## Endpoints

- [01-List all approval rules for a merge request [GET]](./01-list-all-approval-rules-for-a-merge-request-get.md)
- [02-Create an approval rule for a merge request [POST]](./02-create-an-approval-rule-for-a-merge-request-post.md)
- [03-Retrieve an approval rule for a specific merge request [GET]](./03-retrieve-an-approval-rule-for-a-specific-merge-request-get.md)
- [04-Update an approval rule for a merge request [PUT]](./04-update-an-approval-rule-for-a-merge-request-put.md)
- [05-Delete an approval rule for a merge request [DEL]](./05-delete-an-approval-rule-for-a-merge-request-del.md)
- [06-Retrieve MR approval settings for a project [GET]](./06-retrieve-mr-approval-settings-for-a-project-get.md)
- [07-Update MR approval settings for a project [PUT]](./07-update-mr-approval-settings-for-a-project-put.md)
- [08-Retrieve MR approval settings for a group [GET]](./08-retrieve-mr-approval-settings-for-a-group-get.md)
- [09-Update MR approval settings for a group [PUT]](./09-update-mr-approval-settings-for-a-group-put.md)
- [10-Retrieve approval state for a merge request [GET]](./10-retrieve-approval-state-for-a-merge-request-get.md)
- [11-Change approval-related configuration [POST]](./11-change-approval-related-configuration-post.md)
- [12-Approve merge request [POST]](./12-approve-merge-request-post.md)
- [13-Unapprove a merge request [POST]](./13-unapprove-a-merge-request-post.md)
- [14-Reset approvals for a merge request [PUT]](./14-reset-approvals-for-a-merge-request-put.md)
- [15-Retrieve approval details for a merge request [GET]](./15-retrieve-approval-details-for-a-merge-request-get.md)
