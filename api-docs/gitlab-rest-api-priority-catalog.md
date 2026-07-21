# GitLab REST API 우선 검토 카탈로그

> **출처**: `gitlab-api-priority-filter.md`의 우선순위 분류 + `gitlab_rest_defuddle_markdown/` 디렉터리의 API 명세 `index.md` 통합

## 분류 기준

- 대상 역할: 팀장 `Maintainer`, 팀원 `Developer`
- 목표: 팀 프로젝트 시작 지원, 통합 대시보드, 행동 가능한 알림, 반복 작업 자동화
- 원칙: 교육기관 GitLab 인스턴스 전체를 관리해야 하는 기능은 제외

---

## Base URL

```
https://{hostname}/api/v4
```

---

# P0 — 통합 대시보드와 알림의 핵심

---

## 129-projects

접근 가능한 프로젝트의 기본 정보와 상태를 조회하고, 프로젝트 단위 설정을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | List all project security settings | GET |
| 02 | Update project security settings | PUT |
| 03 | List all Terraform state protection rules for a project | GET |
| 04 | Create a Terraform state protection rule for a project | POST |
| 05 | Update a Terraform state protection rule for a project | PATCH |
| 06 | Delete a Terraform state protection rule | DEL |
| 07 | Search on GitLab within a project | GET |
| 08 | List all personal projects for a user | GET |
| 09 | List all projects contributions for a user | GET |
| 10 | List all projects starred by a user | GET |
| 11 | Restore a project marked for deletion | POST |
| **12** | **List all projects** | **GET** |
| 13 | Create a project | POST |
| 14 | Create a project for a user | POST |
| 15 | List all groups available to invite to a project | GET |
| **16** | **Retrieve a project** | **GET** |
| 17 | Update a project | PUT |
| 18 | Delete a project | DEL |
| 19 | Create a fork of a project | POST |
| 20 | Delete a fork relationship | DEL |
| 21 | List all forks of a project | GET |
| 22 | Check pages access of this project | GET |
| 23 | Archive a project | POST |
| 24 | Unarchive a project | POST |
| 25 | Star a project | POST |
| 26 | Unstar a project | POST |
| 27 | List all users who starred a project | GET |
| 28 | Retrieve programming language usage information | GET |
| 29 | Create a fork relationship | POST |
| 30 | Share a project with a group | POST |
| 31 | Delete a shared project link in a group | DEL |
| 32 | Import members | POST |
| **33** | **List all members of a project** | **GET** |
| 34 | List all ancestor groups | GET |
| 35 | List all invited groups in a project | GET |
| 36 | Start the housekeeping task for a project | POST |
| 37 | Start a task to recalculate repository size for a project | POST |
| 38 | Transfer a project to another namespace | PUT |
| 39 | List all transferable namespaces for a project | GET |
| 40 | Retrieve the path to repository storage | GET |
| 41 | List all project audit events | GET |
| 42 | Retrieve a project audit event | GET |
| 43 | Retrieve the statistics of the last 30 days | GET |
| 64 | List all project issues | GET |
| 65 | Create an issue | POST |
| 66 | Retrieve issues statistics for a project | GET |
| 67 | Retrieve a project issue | GET |
| 68 | Update an issue | PUT |
| 69 | Delete an issue | DEL |
| 70 | Update the order of an issue | PUT |
| 71 | Move an issue | POST |
| 72 | Clone an issue | POST |
| 73 | List all merge requests that close an issue on merge | GET |
| 74 | Get projects associated with a runner | GET |
| 75 | List all runners for a project | GET |
| 76 | Assign a runner to a project | POST |
| 77 | Unassign a runner from a project | DEL |
| 78 | Reset the runner registration token for a project | POST |

---

## 67-groups

그룹과 그룹에 속한 프로젝트 정보를 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **19** | **List all groups** | **GET** |
| 20 | Create a group | POST |
| 21 | Update group attributes | PUT |
| **22** | **Retrieve a group** | **GET** |
| 23 | Schedule a group for deletion | DEL |
| 24 | Archive a group | POST |
| 25 | Unarchive a group | POST |
| 26 | Restore a group | POST |
| 27 | List all shared groups | GET |
| 28 | List all invited groups | GET |
| **29** | **List all projects in a group** | **GET** |
| 30 | List all shared projects | GET |
| **31** | **List all subgroups** | **GET** |
| 32 | List all descendant groups | GET |
| 33 | Transfer a project to a group | POST |
| 34 | List all transfer locations for a group | GET |
| 35 | Transfer a group | POST |
| 36 | Transfer a group to an organization | POST |
| 37 | Add a group to a group | POST |
| 38 | Remove a group from a group | DEL |
| 39 | Remove a shared project from a group | DEL |
| 40 | Retrieve a group audit event | GET |
| 41 | List all SAML users | GET |
| 42 | List all provisioned users | GET |
| 03 | List all billable group members | GET |

---

## 91-members

프로젝트·그룹 멤버와 역할을 조회하고 멤버십을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all direct members of a group** | **GET** |
| 02 | Add a member to a group | POST |
| **03** | **List all members of a group** | **GET** |
| 04 | Retrieve a direct group member | GET |
| 05 | Update a group member | PUT |
| 06 | Remove a member from a group | DEL |
| 07 | Retrieve a group member | GET |
| **08** | **List all direct members of a project** | **GET** |
| 09 | Add a member to a project | POST |
| **10** | **List all members of a project** | **GET** |
| 11 | Retrieve a direct project member | GET |
| 12 | Update a project member | PUT |
| 13 | Remove a member from a project | DEL |
| 14 | Retrieve a project member | GET |
| 15 | Set override flag for a member of a group | POST |
| 16 | Remove an LDAP access level override | DEL |
| 17 | Approve a group member | PUT |
| 18 | Approve all pending group members | POST |
| 19 | List all pending group members | GET |
| 20 | Update group membership state for a user | PUT |
| 21 | List all memberships for a billable group member | GET |
| 22 | List all indirect memberships for a billable group member | GET |
| 23 | Remove a billable member from a group | DEL |

---

## 162-users

현재 사용자와 사용자 정보를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **03** | **List all users** | **GET** |
| **05** | **Retrieve a user as a regular user** | **GET** |
| **28** | **Retrieve current user details** | **GET** |
| 08 | Retrieve the status of a user | GET |
| **41** | **Retrieve your user status** | **GET** |
| 38 | List all activity for a user | GET |
| 39 | Set a user status | PUT |
| 40 | Update a user status | PATCH |
| 26 | List all project and group memberships for a user | GET |
| 27 | Retrieve association counts for a user | GET |
| 35 | Retrieve your user preferences | GET |
| 34 | Update your user preferences | PUT |
| 43 | Return the user specific counts | GET |

---

## 52-events

사용자 활동 이벤트를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all visible events for a project** | **GET** |
| **02** | **List all events** | **GET** |
| 03 | Retrieve contribution events for a user | GET |

---

## 158-to-dos

할 일(TODO) 항목을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **03** | **List all to-do items** | **GET** |
| 01 | Create a to-do item for an issuable | POST |
| 04 | Mark a to-do item as done | POST |
| 05 | Mark all to-do items as done | POST |

---

## 139-resource-events

리소스 이벤트(iteration, weight, state, label, milestone 변경)를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Get a list of issue resource iteration events | GET |
| 05 | Get a list of issue resource state events | GET |
| 07 | Get a list of merge request resource state events | GET |
| 11 | Get a list of issue resource label events | GET |
| 13 | Get a list of merge request resource label events | GET |
| 17 | List project Issue milestone events | GET |
| 19 | List project Merge request milestone events | GET |

---

## 74-issues

이슈, 참여자, 관련 MR, 시간 기록, 이슈 연결을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **List all issues for the currently authenticated user** | **GET** |
| **03** | **Retrieve an issue** | **GET** |
| 01 | Retrieve issues statistics for the currently authenticated user | GET |
| 09 | List all merge requests related to an issue | GET |
| **10** | **List all participants in an issue** | **GET** |
| 04 | Set the estimated time for an issue | POST |
| 05 | Reset the estimated time for an issue | POST |
| 06 | Add spent time for an issue | POST |
| 07 | Reset spent time for an issue | POST |
| 08 | Retrieve time tracking stats for an issue | GET |
| 12 | List all issue links | GET |
| 13 | Create an issue link | POST |
| 14 | Retrieve an issue link | GET |
| 15 | Delete an issue link | DEL |

---

## 93-merge-requests

MR 목록·상세·리뷰어·참여자·파이프라인·변경 사항을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **09** | **List all merge requests** | **GET** |
| **10** | **List all group merge requests** | **GET** |
| **16** | **List all project merge requests** | **GET** |
| **19** | **Retrieve a merge request** | **GET** |
| **21** | **Retrieve merge request participants** | **GET** |
| **22** | **Retrieve merge request reviewers** | **GET** |
| **27** | **Retrieve merge request changes** | **GET** |
| **30** | **List all merge request pipelines** | **GET** |
| **36** | **List all issues that close on merge** | **GET** |
| **37** | **List all issues related to the merge request** | **GET** |
| 17 | Create a merge request | POST |
| 20 | Update a merge request | PUT |
| 18 | Delete a merge request | DEL |
| 23 | Retrieve merge request commits | GET |
| 28 | List all merge request diffs | GET |
| 29 | Retrieve merge request raw diffs | GET |
| 31 | Create a merge request pipeline | POST |
| 32 | Merge a merge request | PUT |
| 34 | Cancel merge when pipeline succeeds | POST |
| 35 | Rebase a merge request | PUT |
| 11 | Set the estimated time for a merge request | POST |
| 15 | Retrieve time tracking stats for a merge request | GET |

---

## 119-pipelines

파이프라인·잡·커밋 상태를 조회하고 일부 실행 흐름을 제어한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all project pipelines** | **GET** |
| **03** | **Retrieve the latest pipeline** | **GET** |
| **04** | **Retrieve a pipeline** | **GET** |
| **06** | **List all jobs by pipeline** | **GET** |
| **10** | **Retrieve a test report for a pipeline** | **GET** |
| **11** | **Retrieve a test report summary for a pipeline** | **GET** |
| 02 | Create a pipeline | POST |
| 05 | Delete a pipeline | DEL |
| 09 | List all pipeline variables | GET |
| 12 | Update pipeline metadata | PUT |
| **13** | **Retry jobs in a pipeline** | **POST** |
| 14 | Cancel all jobs for a pipeline | POST |

---

## 24-ci-jobs

프로젝트의 CI 작업 목록과 상세를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all jobs for a project** | **GET** |
| **02** | **Retrieve a job** | **GET** |
| 03 | Get a trace of a specific job of a project | GET |
| 04 | Cancel a job | POST |
| **05** | **Retry a job** | **POST** |
| 06 | Erase a job | POST |

---

## 80-jobs

Runner가 처리한 작업 및 아티팩트 관련 API.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | List all jobs processed by a runner | GET |
| 07 | Download the artifacts file for job | GET |

---

## 35-commit-statuses

커밋 상태를 조회하고 생성한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all commit statuses** | **GET** |
| 02 | Create or update a commit pipeline status | POST |

---

# P1 — 프로젝트 시작과 팀 개발 흐름에 유용한 카테고리

---

## 68-hooks

프로젝트·그룹 이벤트를 외부 HTTP 엔드포인트로 전달하는 webhook을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **27** | **List all webhooks for a project** | **GET** |
| **28** | **Add a webhook to a project** | **POST** |
| **29** | **Retrieve a project webhook** | **GET** |
| 30 | Update a project webhook | PUT |
| **31** | **Delete a project webhook** | **DEL** |
| 33 | Trigger a test webhook | POST |
| 34 | Resend a webhook event | POST |
| 01 | List all group hooks | GET |
| 02 | Create a group hook | POST |
| 03 | Retrieve a group hook | GET |
| 04 | Update a group hook | PUT |
| 05 | Delete a group hook | DEL |
| 12 | Resend a webhook event | POST |

---

## 73-invitations

그룹·프로젝트 초대의 대기·수락 전 단계를 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **List all pending invitations for a group** | **GET** |
| **06** | **List all pending invitations for a project** | **GET** |
| 01 | Add a member to a group (via invitation) | POST |
| 03 | Update an invitation to a group | PUT |
| 04 | Delete an invitation to a group | DEL |
| 05 | Add a member to a project (via invitation) | POST |
| 07 | Update an invitation to a project | PUT |
| 08 | Delete an invitation to a project | DEL |

---

## 71-integrations

GitLab 프로젝트와 외부 서비스(Jenkins, Jira, Mattermost 등)의 통합 설정을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **04** | **List all active integrations** | **GET** |
| **57** | **Get an integration settings** | **GET** |
| 25 / 80 | Create/Edit Jenkins integration | PUT |
| 26 / 81 | Create/Edit Jira integration | PUT |
| 30 / 85 | Create/Edit Mattermost Slash Commands integration | PUT |
| 43 / 98 | Create/Edit Mattermost integration | PUT |
| 16 / 71 | Create/Edit Discord integration | PUT |
| 41 / 96 | Create/Edit Slack integration | PUT |
| 42 / 97 | Create/Edit Microsoft Teams integration | PUT |
| 56 / 111 | Disable an integration | DEL |

가장 통합 가능성이 높은 서비스 (Jenkins, Jira, Mattermost)의 PUT 엔드포인트는 **리스트 통합 조회 후 개별 설정 조회** 순서로 검증한다.

---

## 127-project-templates

프로젝트 템플릿 후보를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all templates of a particular type** | **GET** |
| 02 | Retrieve a template of a particular type | GET |

---

## 156-templates

라이선스, .gitignore, CI/CD YAML, Dockerfile 템플릿을 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | List all license templates | GET |
| 02 | Retrieve a license template | GET |
| 03 | List all .gitignore templates | GET |
| 04 | Retrieve a .gitignore template | GET |
| 05 | List all GitLab CI/CD YAML templates | GET |
| 06 | Retrieve a GitLab CI/CD YAML template | GET |
| 07 | List all Dockerfile templates | GET |
| 08 | Retrieve a Dockerfile template | GET |

---

## 29-ci-triggers

외부에서 파이프라인을 트리거하는 토큰을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Trigger a pipeline with a token** | **POST** |
| **02** | **List all project trigger tokens** | **GET** |
| 03 | Create a trigger token | POST |
| 04 | Retrieve trigger token details | GET |
| 05 | Update a pipeline trigger token | PUT |
| 06 | Delete a pipeline trigger token | DEL |

---

## 118-pipeline-schedules

정기 파이프라인 실행 일정을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all pipeline schedules** | **GET** |
| **08** | **Run a pipeline schedule** | **POST** |
| 02 | Create a pipeline schedule | POST |
| 03 | Retrieve a pipeline schedule | GET |
| 04 | Update a pipeline schedule | PUT |
| 05 | Delete a pipeline schedule | DEL |
| 06 | List all pipelines triggered by a pipeline schedule | GET |
| 09 | Create a variable for a pipeline schedule | POST |
| 10 | Retrieve a variable for a pipeline schedule | GET |

---

## 30-ci-variables

CI/CD 변수(그룹·프로젝트·인스턴스 수준)를 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all group variables** | **GET** |
| **06** | **List all project variables** | **GET** |
| 02 | Create a group variable | POST |
| 03 | Retrieve details of a group variable | GET |
| 04 | Update a group variable | PUT |
| 05 | Delete a group variable | DEL |
| 07 | Create a variable | POST |
| 08 | Retrieve a single variable | GET |
| 09 | Update a variable | PUT |
| 10 | Delete a variable | DEL |
| 11 | List all instance variables | GET |

---

## 25-ci-lint

CI/CD 설정을 검증한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Validate existing CI/CD configuration** | **GET** |
| 02 | Validate a CI/CD configuration | POST |

---

## 21-branches

브랜치를 조회하고 생성·삭제·보호 설정을 다룬다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all repository branches** | **GET** |
| **04** | **Retrieve a repository branch** | **GET** |
| 02 | Create a repository branch | POST |
| 03 | Check if a branch exists | HEAD |
| 05 | Delete a repository branch | DEL |
| 06 | Protect a single branch | PUT |
| 07 | Unprotect a single branch | PUT |
| 08 | Delete all merged branches | DEL |

---

## 131-protected-branches

보호된 브랜치 규칙을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all protected branches** | **GET** |
| **03** | **Retrieve a protected branch** | **GET** |
| 02 | Protect a repository branch | POST |
| 04 | Update a protected branch | PATCH |
| 05 | Unprotect repository branches | DEL |

---

## 132-protected-environments

보호된 환경(배포 대상)을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all protected environments for a project** | **GET** |
| **03** | **Retrieve a protected environment for a project** | **GET** |
| 02 | Protect an environment for a project | POST |
| 04 | Update a protected environment for a project | PUT |
| 05 | Unprotect a protected environment for a project | DEL |

---

## 133-protected-tags

보호된 태그 규칙을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all protected tags** | **GET** |
| **03** | **Retrieve a protected tag** | **GET** |
| 02 | Protect a repository tag | POST |
| 04 | Unprotect repository tags | DEL |

---

## 135-push-rules

Push 규칙을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Retrieve the push rules of a group** | **GET** |
| **05** | **Retrieve the push rules of a project** | **GET** |
| 02 | Add push rules to a group | POST |
| 03 | Update push rules of a group | PUT |
| 04 | Delete the push rules of a group | DEL |
| 06 | Add push rules to a project | POST |
| 07 | Update an existing project push rule | PUT |
| 08 | Delete the push rules of a project | DEL |

---

## 155-tags

저장소 태그를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Get a project repository tags** | **GET** |
| **03** | **Get a single repository tag** | **GET** |
| 02 | Create a new repository tag | POST |
| 04 | Delete a repository tag | DEL |
| 05 | Get a tag's signature | GET |

---

## 36-commits

커밋을 조회하고 생성한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all repository commits** | **GET** |
| **03** | **Retrieve a commit** | **GET** |
| **04** | **Retrieve a commit diff** | **GET** |
| **11** | **List all merge requests for a commit** | **GET** |
| 02 | Create a commit | POST |
| 05 | List all commit comments | GET |
| 06 | Create a comment on a commit | POST |
| 07 | Retrieve a commit sequence | GET |
| 08 | Cherry-pick a commit | POST |
| 09 | Revert a commit | POST |
| 10 | List all references a commit is pushed to | GET |
| 12 | Retrieve a commit signature | GET |

---

## 57-files

저장소 파일을 조회하고 생성·수정·삭제한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **03** | **Retrieve a raw file from a repository** | **GET** |
| **05** | **Retrieve a file from a repository** | **GET** |
| 01 | Retrieve file blame metadata | HEAD |
| 02 | Retrieve file blame history from a repository | GET |
| 04 | Retrieve file metadata | HEAD |
| 06 | Create a file in a repository | POST |
| 07 | Update a file in a repository | PUT |
| 08 | Delete a file in a repository | DEL |

---

## 138-repositories

저장소 트리, Blob, 아카이브, 비교, 기여자 등을 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Get a project repository tree** | **GET** |
| **02** | **Get raw blob contents from the repository** | **GET** |
| **04** | **Get an archive of the repository** | **GET** |
| **05** | **Compare two branches, tags, or commits** | **GET** |
| **07** | **Get repository contributors** | **GET** |
| **09** | **Generate a changelog section for a release (preview)** | **GET** |
| 03 | Get a blob from the repository | GET |
| 06 | Get repository health | GET |
| 08 | Get the common ancestor between commits | GET |
| 10 | Generate a changelog section for a release and commit | POST |

---

## 166-web-commits

웹 커밋 공개 서명 키 조회.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Retrieve the public signing key | GET |

---

## 46-discussions

MR·이슈·커밋·스니펫·에픽 토론을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Get a list of issue discussions** | **GET** |
| **18** | **Get a list of merge request discussions** | **GET** |
| **27** | **Get a list of commit discussions** | **GET** |
| 05 | Get comments in a single issue discussion | GET |
| 22 | Get comments in a single merge request discussion | GET |
| 30 | Get comments in a single commit discussion | GET |
| 02 | Create a new issue discussion | POST |
| 19 | Create a new merge request discussion | POST |
| 04 | Resolve/unresolve an existing issue discussion | PUT |
| 21 | Resolve/unresolve an existing merge request discussion | PUT |

---

## 101-notes

이슈·MR·스니펫·위키·에픽·취약점 노트(댓글)를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Get a list of issue notes** | **GET** |
| **06** | **Get a list of merge request notes** | **GET** |
| 02 | Create a new issue note | POST |
| 03 | Get a single issue note | GET |
| 04 | Update an existing issue note | PUT |
| 05 | Delete a issue note | DEL |
| 07 | Create a new merge request note | POST |
| 08 | Get a single merge request note | GET |
| 09 | Update an existing merge request note | PUT |
| 10 | Delete a merge request note | DEL |

---

## 154-suggestions

MR 코드 제안(Suggestion)을 적용한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Apply a suggestion to a merge request | PUT |
| 02 | Apply multiple suggestions to a merge request | PUT |

---

## 84-labels

프로젝트·그룹 라벨을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all project labels** | **GET** |
| **05** | **Retrieve a project label** | **GET** |
| **10** | **List all group labels** | **GET** |
| 02 | Create a project label | POST |
| 03 | Update an existing label | PUT |
| 04 | Delete an existing label | DEL |
| 08 | Promote a label to a group label | PUT |
| 11 | Create a group label | POST |
| 12 | Update a group label | PUT |
| 13 | Delete a group label | DEL |

---

## 99-milestones

프로젝트·그룹 마일스톤을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all project milestones** | **GET** |
| **03** | **Retrieve a project milestone** | **GET** |
| **06** | **List all issues for a project milestone** | **GET** |
| **07** | **List all merge requests for a project milestone** | **GET** |
| **10** | **List all group milestones** | **GET** |
| 02 | Create a project milestone | POST |
| 04 | Update a project milestone | PUT |
| 05 | Delete a project milestone | DEL |
| 08 | Promote a project milestone to a group milestone | POST |
| 09 | List all burndown chart events for a milestone | GET |
| 11 | Create a group milestone | POST |
| 12 | Retrieve a group milestone | GET |

---

## 75-iterations

프로젝트·그룹 이터레이션을 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all project iterations** | **GET** |
| **02** | **List all group iterations** | **GET** |

---

## 20-boards

프로젝트·그룹 이슈 보드를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **List all group issue boards in a group** | **GET** |
| **11** | **List all project issue boards** | **GET** |
| **13** | **Retrieve an issue board** | **GET** |
| **16** | **List all board lists in an issue board** | **GET** |
| 01 | Create a group issue board | POST |
| 04 | Retrieve a group issue board | GET |
| 05 | Update a group issue board | PUT |
| 12 | Create an issue board | POST |
| 14 | Update an issue board | PUT |
| 15 | Delete an issue board | DEL |
| 17 | Create an issue board list | POST |
| 18 | Retrieve a board list | GET |

---

## 136-releases

릴리스와 릴리스 링크를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **06** | **List all releases in a group** | **GET** |
| **07** | **List all releases in a project** | **GET** |
| **09** | **Retrieve a release by tag name** | **GET** |
| 01 | List all release links | GET |
| 08 | Create a release | POST |
| 10 | Update a release | PUT |
| 11 | Delete a release | DEL |
| 12 | Generate release evidence | POST |

---

## 49-environments

배포 환경을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all environments** | **GET** |
| **05** | **Retrieve an environment** | **GET** |
| 02 | Create an environment | POST |
| 03 | Update an existing environment | PUT |
| 04 | Delete an environment | DEL |
| 07 | Stop an environment | POST |

---

## 45-deploy-resources

배포 키와 배포(deployment)를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **List all project deployments** | **GET** |
| **04** | **Retrieve a deployment** | **GET** |
| **07** | **List all merge requests associated with a deployment** | **GET** |
| 01 | List all project deploy keys for a user | GET |
| 03 | Create a deployment | POST |
| 05 | Update a deployment | PUT |
| 06 | Delete a deployment | DEL |
| 08 | Approve or reject a deployment | POST |
| 09 | List all deploy tokens | GET |

---

## 79-job-artifacts

CI 작업 아티팩트를 조회·다운로드·삭제한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Retrieve job artifacts** | **GET** |
| **02** | **Download the artifacts archive from a job** | **GET** |
| **04** | **List all files in an artifacts archive** | **GET** |
| 03 | Delete job artifacts | DEL |
| 05 | Retain job artifacts | POST |
| 06 | Delete all job artifacts in a project | DEL |

---

## 145-search

프로젝트·코드·인스턴스 검색을 지원한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **04** | **Search an instance** | **GET** |
| **05** | **Search on GitLab within a group** | **GET** |
| **06** | **Search on GitLab within a project** | **GET** |
| 01 | Search project code using natural language | GET |

---

## 34-code-search

코드 검색 인덱싱 관련 API. (Zoekt 기반, 인스턴스 설정 필요)

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Triggers indexing for the specified project | PUT |
| 03 | Get all the Zoekt nodes | GET |
| 04 | Get all the indexed namespaces for this node | GET |

---

## 89-markdown

Markdown 콘텐츠를 HTML로 렌더링한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Render Markdown content** | **POST** |

---

## 11-applications

(관리자 전용) 인스턴스 애플리케이션 등록 및 관리. OAuth2 앱 등록은 `103-oauth-applications` 참고.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 02 | List all applications | GET |
| 03 | Retrieve an application | GET |

---

## 103-oauth-applications

OAuth2 애플리케이션 서버 설정 조회.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | server_config | GET |

---

## 159-token-exchange

단일 모듈식 서비스 대상 단기 JWT 발급.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Issue a short-lived JWT for a single modular-service audience | POST |

---

# P2 — 유용하지만 실제 사용 방식 확인 후 검토할 카테고리

---

## 12-approval-rules

MR 승인 규칙을 조회하고 관리한다. (GitLab 에디션·인스턴스 정책 지원 확인 필요)

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Get all project approval rules** | **GET** |
| **05** | **List all approval rules for a group** | **GET** |
| **08** | **List all approval rules for a project** | **GET** |
| 02 | Create new approval rule | POST |
| 03 | Update approval rule | PUT |
| 04 | Delete an approval rule | DEL |

---

## 92-merge-request-approvals

MR 승인 상태 및 설정을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **06** | **Retrieve MR approval settings for a project** | **GET** |
| **10** | **Retrieve approval state for a merge request** | **GET** |
| **15** | **Retrieve approval details for a merge request** | **GET** |
| 01 | List all approval rules for a merge request | GET |
| 12 | Approve merge request | POST |
| 13 | Unapprove a merge request | POST |

---

## 54-external-status-checks

외부 도구의 MR 상태 확인 서비스를 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **Retrieve project external status check services** | **GET** |
| **06** | **List all status checks for a merge request** | **GET** |
| 01 | Create external status check service | POST |
| 03 | Update external status check service | PUT |
| 04 | Delete external status check service | DEL |
| 05 | Update status of an external status check | POST |

---

## 94-merge-trains

병합 대기열을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all merge trains for a project** | **GET** |
| **03** | **Retrieve merge train status** | **GET** |
| 02 | List all merge requests in a merge train | GET |
| 04 | Add a merge request to a merge train | POST |

---

## 107-packages

프로젝트·그룹 패키지를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all packages for a project** | **GET** |
| **08** | **List all packages for a group** | **GET** |
| 02 | Retrieve a project package | GET |
| 03 | Delete a project package | DEL |
| 05 | List all package files | GET |
| 07 | Download a package file | GET |

---

## 38-container-registry

컨테이너 레지스트리 저장소와 태그를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all registry repositories for a project** | **GET** |
| **03** | **List all registry repository tags for a project** | **GET** |
| **07** | **List all registry repositories for a group** | **GET** |
| 02 | Delete registry repository | DEL |
| 04 | Delete multiple registry repository tags | DEL |
| 05 | Retrieve details of a registry repository tag | GET |
| 06 | Delete a registry repository tag | DEL |

---

## 137-remote-mirrors

외부 저장소로의 푸시 미러를 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List the project's remote mirrors** | **GET** |
| 02 | Create remote mirror for a project | POST |
| 04 | Update the attributes of a single remote mirror | PUT |
| 05 | Delete a single remote mirror | DEL |
| 06 | Triggers a push mirror operation | POST |

---

## 125-project-mirrors

프로젝트 풀 미러링(Pull mirroring)을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **03** | **Retrieve project pull mirror details** | **GET** |
| 01 | Start the pull mirroring process for a project | POST |
| 02 | Update project pull mirroring settings | PUT |

---

## 153-submodules

서브모듈 참조를 업데이트한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Update existing submodule reference in repository | PUT |

---

## 50-epics

그룹 에픽과 에픽 관계를 조회하고 관리한다. (Ultimate 에디션 필요 가능)

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **09** | **List all group epics** | **GET** |
| **11** | **Get details of an epic** | **GET** |
| **24** | **List all issues for an epic** | **GET** |
| 01 | List all related epic links for a group | GET |
| 05 | List all epic boards in a group | GET |
| 13 | Create a new epic | POST |
| 14 | Update an epic | PUT |
| 15 | Destroy an epic | DEL |
| 22 | Add an issue to an epic | POST |
| 23 | Remove an issue from the epic | DEL |

---

## 40-dora-metrics

DORA 메트릭(배포 빈도, 리드 타임 등)을 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **Retrieve project-level DORA metrics** | **GET** |
| 02 | Retrieve group-level DORA metrics | GET |

---

## 10-analytics

배포 빈도, 이슈·MR 생성 수, 멤버 추가 수 등 분석 데이터를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List deployment frequencies for the project** | **GET** |
| **05** | **Retrieve count of recently created issues for a group** | **GET** |
| **06** | **Retrieve count of recently created merge requests for a group** | **GET** |
| **07** | **Retrieve count of members recently added to a group** | **GET** |

---

## 33-code-review-analytics

코드 리뷰 활동 정보를 조회한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List code review information about project** | **GET** |

---

## 58-freeze-periods

배포 동결 기간을 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all freeze periods** | **GET** |
| 02 | Create a freeze period | POST |
| 03 | Retrieve a freeze period | GET |
| 04 | Update a freeze period | PUT |
| 05 | Delete a freeze period | DEL |

---

## 167-wikis

그룹·프로젝트 Wiki 페이지를 조회하고 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **01** | **List all wiki pages for a group** | **GET** |
| **07** | **List all wiki pages for a project** | **GET** |
| **09** | **Retrieve a wiki page for a project** | **GET** |
| 02 | Create a wiki page for a group | POST |
| 03 | Retrieve a wiki page for a group | GET |
| 04 | Update a wiki page for a group | PUT |
| 05 | Delete a wiki page for a group | DEL |
| 08 | Create a wiki page for a project | POST |
| 10 | Update a wiki page for a project | PUT |
| 11 | Delete a wiki page for a project | DEL |

---

## 76-jira-connect-subscriptions

Jira Connect 네임스페이스 구독을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Subscribe a namespace to a Jira Connect installation | POST |

---

## 77-jira-forge-installation

GitLab for Jira (Forge) 설치 인스턴스 URL 업데이트 및 시스템 토큰 등록.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| 01 | Update the GitLab for Jira (Forge) installation instance URL | PUT |
| 02 | Register the GitLab for Jira (Forge) system token for direct dev-info sync | POST |

---

## 78-jira-forge-subscriptions

GitLab for Jira (Forge) 네임스페이스 구독을 관리한다.

| # | 엔드포인트 | Method |
| --- | --- | --- |
| **02** | **List GitLab for Jira (Forge) namespace subscriptions** | **GET** |
| 01 | Create a GitLab for Jira (Forge) namespace subscription | POST |
| 03 | Delete a GitLab for Jira (Forge) namespace subscription | DEL |

---

# OAuth2 인증 (POC 기본 인증 방식)

OAuth2는 POC의 기본 인증 방식이다. `https://lab.ssafy.com/-/user_settings/applications`에서 사용자 계정으로 앱 등록이 확인되었다.

## 지원 흐름

| 흐름 | 권장 대상 | 특징 |
| --- | --- | --- |
| **PKCE Authorization Code** | SPA, 모바일 앱 | client_secret 불필요, 가장 안전 |
| **Authorization Code** | 서버사이드 앱 (EC2 백엔드) | client_secret 필요, Confidential 앱 |
| **Device Authorization Grant** | 헤드리스/CLI 환경 | 보조 기기로 브라우저 인증 |

## 권장 scope 전략

| scope | 용도 |
| --- | --- |
| `read_api` | 읽기 전용 대시보드 (팀원) |
| `api` | 읽기+쓰기 (팀장 전용) |
| `read_user` | 사용자 기본 정보 |
| `openid` | OpenID Connect |

## 주요 엔드포인트

| 엔드포인트 | 설명 |
| --- | --- |
| `GET /oauth/authorize` | 권한 부여 코드 요청 (사용자 리다이렉트) |
| `POST /oauth/token` | 액세스 토큰 발급 / 갱신 |
| `POST /oauth/revoke` | 토큰 취소 |
| `GET /oauth/token/info` | 토큰 정보 조회 |
| `POST /oauth/authorize_device` | 기기 인증 권한 부여 요청 |

## 토큰 응답 예시

```json
{
  "access_token": "de6780bc506a0446309bd9362820ba8aed28aa506c71eedbe1c5c4f9dd350e54",
  "token_type": "bearer",
  "expires_in": 7200,
  "refresh_token": "8257e65c97202ed1726cf9571600918f3bffb2544b26e00a61df9897668c33a1",
  "created_at": 1607635748
}
```

## 첫 API 검증 순서

1. **현재 사용자·프로젝트·멤버 조회**: `162-users` → `129-projects` → `91-members`
2. **읽기 전용 대시보드 데이터**: `93-merge-requests`, `74-issues`, `119-pipelines`, `52-events`, `158-to-dos`
3. **팀 시작 자동화 후보**: `127-project-templates`, `156-templates`, `73-invitations`
4. **이벤트 수신**: `68-hooks` (프로젝트 webhook)
5. **자동화 후보**: `71-integrations`, `29-ci-triggers`, `118-pipeline-schedules` (팀장 토큰)
6. **보안·리뷰 보조**: `132-protected-environments`, `135-push-rules`, `54-external-status-checks`
7. **쓰기 작업 확장**: 멤버, 라벨, 마일스톤, 브랜치 보호 규칙 (성공·실패 기록 후)
