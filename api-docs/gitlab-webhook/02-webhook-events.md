---
title: "Webhook events"
source: "https://docs.gitlab.com/user/project/integrations/webhook_events/"
created: 2026-07-20
description: "GitLab 웹훅 이벤트 및 페이로드 목록. JSON 예제 포함."
---

/

---

웹훅을 사용하여 GitLab을 외부 애플리케이션에 연결하고 워크플로우를 자동화하세요. GitLab에서 특정 이벤트가 발생하면 웹훅이 구성된 엔드포인트로 상세 정보가 포함된 HTTP POST 요청을 전송합니다. 수동 개입 없이 코드 변경, 배포, 댓글 및 기타 활동에 반응하는 자동화된 프로세스를 구축하세요.

이 페이지는 [프로젝트 웹훅](https://docs.gitlab.com/user/project/integrations/webhooks/) 및 [그룹 웹훅](https://docs.gitlab.com/user/project/integrations/webhooks/#group-webhooks)에 대해 트리거되는 이벤트를 설명합니다.

시스템 웹훅에 대해 트리거되는 이벤트 목록은 [시스템 웹훅](https://docs.gitlab.com/administration/system_hooks/)을 참조하세요.

## 프로젝트 및 그룹 웹훅 모두에 대해 트리거되는 이벤트

| 이벤트 유형 | 트리거 |
| --- | --- |
| [댓글 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#comment-events) | 커밋, 머지 리퀘스트, 이슈 및 코드 스니펫에 새 댓글이 작성되거나 편집됨 <sup>1</sup> |
| [배포 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#deployment-events) | 배포가 시작, 성공, 실패 또는 취소됨 |
| [이모지 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#emoji-events) | 이모지 반응이 추가되거나 제거됨 |
| [기능 플래그 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#feature-flag-events) | 기능 플래그가 켜지거나 꺼짐 |
| [Job 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#job-events) | Job 상태가 변경됨 |
| [머지 리퀘스트 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#merge-request-events) | 머지 리퀘스트가 생성, 편집, 병합 또는 종료되거나 소스 브랜치에 커밋이 추가됨 |
| [마일스톤 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#milestone-events) | 마일스톤이 생성, 종료, 재개 또는 삭제됨 |
| [파이프라인 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#pipeline-events) | 파이프라인 상태가 변경됨 |
| [프로젝트 또는 그룹 액세스 토큰 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#project-and-group-access-token-events) | 프로젝트 또는 그룹 액세스 토큰이 7일, 30일 또는 60일 내에 만료 예정 |
| [푸시 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#push-events) | 리포지토리에 푸시가 발생함 |
| [릴리스 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#release-events) | 릴리스가 생성, 편집 또는 삭제됨 |
| [태그 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#tag-events) | 리포지토리에서 태그가 생성 또는 삭제됨 |
| [취약점 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#vulnerability-events) | 취약점이 생성 또는 업데이트됨 |
| [위키 페이지 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#wiki-page-events) | 위키 페이지가 생성, 편집 또는 삭제됨 |
| [작업 항목 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#work-item-events) | 새 작업 항목이 생성되거나 기존 항목이 편집, 종료 또는 재개됨 |

각주:

1. 댓글이 편집될 때 트리거되는 댓글 이벤트는 GitLab 16.11에서 [도입](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/127169)되었습니다.

## 그룹 웹훅에만 트리거되는 이벤트

| 이벤트 유형 | 트리거 |
| --- | --- |
| [그룹 멤버 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#group-member-events) | 사용자가 그룹에 추가되거나 제거되거나, 사용자의 액세스 수준 또는 액세스 만료일이 변경됨 |
| [프로젝트 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#project-events) | 그룹에서 프로젝트가 생성 또는 삭제됨 |
| [하위 그룹 이벤트](https://docs.gitlab.com/user/project/integrations/webhook_events/#subgroup-events) | 그룹에서 하위 그룹이 생성 또는 제거됨 |

> [!type-note] 유형 노트
> 작성자가 [GitLab 프로필](https://gitlab.com/-/user_settings/profile)에 공개 이메일을 등록하지 않은 경우 웹훅 페이로드의 `email` 속성은 `[REDACTED]` 값을 표시합니다.

## 푸시 이벤트

푸시 이벤트는 리포지토리에 푸시할 때 트리거됩니다. 단, 다음 경우는 제외됩니다:

- 태그를 푸시하는 경우
- 기본적으로 단일 푸시에 3개 이상의 브랜치에 대한 변경 사항이 포함된 경우 ([`push_event_hooks_limit` 설정](https://docs.gitlab.com/api/settings/#available-settings)에 따라 다름)

한 번에 20개 이상의 커밋을 푸시하면 페이로드의 `commits` 속성에는 최신 20개 커밋에 대한 정보만 포함됩니다. 상세한 커밋 데이터 로딩은 비용이 많이 들기 때문에 성능상의 이유로 이 제한이 있습니다. `total_commits_count` 속성에는 실제 커밋 수가 포함됩니다.

> [!type-note] 유형 노트
> 별도의 설정인 `push_event_activities_limit`는 GitLab이 활동 피드에 개별 푸시 이벤트를 생성할지 일괄 푸시 이벤트를 생성할지 제어합니다. 자세한 내용은 [푸시 이벤트 활동 제한](https://docs.gitlab.com/administration/settings/push_event_activities_limit/)을 참조하세요.

새 커밋 없이 브랜치를 생성하고 푸시하는 경우 페이로드의 `commits` 속성은 비어 있습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Push Hook
```

페이로드 예제:

```json
{
  "object_kind": "push",
  "event_name": "push",
  "before": "95790bf891e76fee5e1747ab589903a6a1f80f22",
  "after": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
  "ref": "refs/heads/master",
  "ref_protected": true,
  "checkout_sha": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
  "message": "Hello World",
  "user_id": 4,
  "user_name": "John Smith",
  "user_username": "jsmith",
  "user_email": "john@example.com",
  "user_avatar": "https://s.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?s=8://s.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?s=80",
  "project_id": 15,
  "project": {
    "id": 15,
    "name": "Diaspora",
    "description": "",
    "web_url": "http://example.com/mike/diaspora",
    "avatar_url": null,
    "git_ssh_url": "git@example.com:mike/diaspora.git",
    "git_http_url": "http://example.com/mike/diaspora.git",
    "namespace": "Mike",
    "visibility_level": 0,
    "path_with_namespace": "mike/diaspora",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "http://example.com/mike/diaspora",
    "url": "git@example.com:mike/diaspora.git",
    "ssh_url": "git@example.com:mike/diaspora.git",
    "http_url": "http://example.com/mike/diaspora.git"
  },
  "commits": [
    {
      "id": "b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
      "message": "Update Catalan translation to e38cb41.\n\nSee https://gitlab.com/gitlab-org/gitlab for more information",
      "title": "Update Catalan translation to e38cb41.",
      "timestamp": "2011-12-12T14:27:31+02:00",
      "url": "http://example.com/mike/diaspora/commit/b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
      "author": {
        "name": "Jordi Mallach",
        "email": "jordi@softcatala.org"
      },
      "added": ["CHANGELOG"],
      "modified": ["app/controller/application.rb"],
      "removed": []
    },
    {
      "id": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
      "message": "fixed readme",
      "title": "fixed readme",
      "timestamp": "2012-01-03T23:36:29+02:00",
      "url": "http://example.com/mike/diaspora/commit/da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
      "author": {
        "name": "GitLab dev user",
        "email": "gitlabdev@dv6700.(none)"
      },
      "added": ["CHANGELOG"],
      "modified": ["app/controller/application.rb"],
      "removed": []
    }
  ],
  "total_commits_count": 4,
  "push_options": {},
  "repository": {
    "name": "Diaspora",
    "url": "git@example.com:mike/diaspora.git",
    "description": "",
    "homepage": "http://example.com/mike/diaspora",
    "git_http_url": "http://example.com/mike/diaspora.git",
    "git_ssh_url": "git@example.com:mike/diaspora.git",
    "visibility_level": 0
  }
}
```

## 태그 이벤트

태그 이벤트는 리포지토리에서 태그를 생성하거나 삭제할 때 트리거됩니다.

기본적으로 단일 푸시에 3개 이상의 태그에 대한 변경 사항이 포함된 경우 이 훅은 실행되지 않습니다. 이 제한은 `push_event_hooks_limit` 설정(기본값: `3`)에 의해 제어되며, 태그와 브랜치 모두에 적용됩니다. 초과 시 해당 푸시 이벤트에 대해 웹훅이 전혀 트리거되지 않습니다.

GitLab Self-Managed 인스턴스의 경우 관리자는 [애플리케이션 설정 API](https://docs.gitlab.com/api/settings/#available-settings)를 사용하여 이 제한을 수정할 수 있습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Tag Push Hook
```

페이로드 예제:

```json
{
  "object_kind": "tag_push",
  "event_name": "tag_push",
  "before": "0000000000000000000000000000000000000000",
  "after": "82b3d5ae55f7080f1e6022629cdb57bfae7cccc7",
  "ref": "refs/tags/v1.0.0",
  "ref_protected": true,
  "checkout_sha": "82b3d5ae55f7080f1e6022629cdb57bfae7cccc7",
  "message": "Tag message",
  "user_id": 1,
  "user_name": "John Smith",
  "user_username": "jsmith",
  "user_email": "john@example.com",
  "user_avatar": "https://s.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?s=8://s.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?s=80",
  "project_id": 1,
  "project": {
    "id": 1,
    "name": "Example",
    "description": "",
    "web_url": "http://example.com/jsmith/example",
    "avatar_url": null,
    "git_ssh_url": "git@example.com:jsmith/example.git",
    "git_http_url": "http://example.com/jsmith/example.git",
    "namespace": "Jsmith",
    "visibility_level": 0,
    "path_with_namespace": "jsmith/example",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "http://example.com/jsmith/example",
    "url": "git@example.com:jsmith/example.git",
    "ssh_url": "git@example.com:jsmith/example.git",
    "http_url": "http://example.com/jsmith/example.git"
  },
  "commits": [],
  "total_commits_count": 0,
  "push_options": {},
  "repository": {
    "name": "Example",
    "url": "ssh://git@example.com/jsmith/example.git",
    "description": "",
    "homepage": "http://example.com/jsmith/example",
    "git_http_url": "http://example.com/jsmith/example.git",
    "git_ssh_url": "git@example.com:jsmith/example.git",
    "visibility_level": 0
  }
}
```

## 작업 항목 이벤트

작업 항목 이벤트는 작업 항목이 생성, 편집, 종료 또는 재개될 때 트리거됩니다. 지원되는 작업 항목 유형은 다음과 같습니다:

- [에픽](https://docs.gitlab.com/user/group/epics/)
- [이슈](https://docs.gitlab.com/user/project/issues/)
- [작업(Task)](https://docs.gitlab.com/user/tasks/)
- [인시던트](https://docs.gitlab.com/operations/incident_management/incidents/)
- [테스트 케이스](https://docs.gitlab.com/ci/test_cases/)
- [요구사항](https://docs.gitlab.com/user/project/requirements/)
- [목표 및 주요 결과(OKR)](https://docs.gitlab.com/user/okrs/)

이슈 및 [Service Desk](https://docs.gitlab.com/user/project/service_desk/) 이슈의 경우 `object_kind`는 `issue`이고 `type`은 `Issue`입니다. 다른 모든 작업 항목의 경우 `object_kind` 필드는 `work_item`이고 `type`은 작업 항목 유형입니다.

작업 항목 유형이 `Epic`인 경우 변경 사항에 대한 이벤트를 받으려면 웹훅이 그룹에 등록되어 있어야 합니다.

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `open`
- `close`
- `reopen`
- `update`

`assignee` 및 `assignee_id` 키는 더 이상 사용되지 않으며 첫 번째 담당자만 포함합니다.

`escalation_status` 및 `escalation_policy` 필드는 인시던트와 같이 [에스컬레이션을 지원](https://docs.gitlab.com/operations/incident_management/paging/#paging)하는 이슈 유형에만 사용할 수 있습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Issue Hook
```

페이로드 예제:

```json
{
  "object_kind": "issue",
  "event_type": "issue",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project": {
    "id": 1,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlabhq/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "git_http_url":"http://example.com/gitlabhq/gitlab-test.git",
    "namespace":"GitlabHQ",
    "visibility_level":20,
    "path_with_namespace":"gitlabhq/gitlab-test",
    "default_branch":"master",
    "ci_config_path": null,
    "homepage":"http://example.com/gitlabhq/gitlab-test",
    "url":"http://example.com/gitlabhq/gitlab-test.git",
    "ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "http_url":"http://example.com/gitlabhq/gitlab-test.git"
  },
  "object_attributes": {
    "id": 301,
    "title": "New API: create/update/delete file",
    "assignee_ids": [51],
    "assignee_id": 51,
    "author_id": 51,
    "project_id": 14,
    "created_at": "2013-12-03T17:15:43Z",
    "updated_at": "2013-12-03T17:15:43Z",
    "updated_by_id": 1,
    "last_edited_at": null,
    "last_edited_by_id": null,
    "relative_position": 0,
    "description": "Create new API for manipulations with repository",
    "milestone_id": null,
    "state_id": 1,
    "confidential": false,
    "discussion_locked": true,
    "due_date": null,
    "start_date": null,
    "moved_to_id": null,
    "duplicated_to_id": null,
    "time_estimate": 0,
    "total_time_spent": 0,
    "time_change": 0,
    "human_total_time_spent": null,
    "human_time_estimate": null,
    "human_time_change": null,
    "weight": null,
    "health_status": "at_risk",
    "type": "Issue",
    "iid": 23,
    "url": "http://example.com/diaspora/issues/23",
    "state": "opened",
    "action": "open",
    "severity": "high",
    "escalation_status": "triggered",
    "escalation_policy": {
      "id": 18,
      "name": "Engineering On-call"
    },
    "labels": [{
        "id": 206,
        "title": "API",
        "color": "#ffffff",
        "project_id": 14,
        "created_at": "2013-12-03T17:15:43Z",
        "updated_at": "2013-12-03T17:15:43Z",
        "template": false,
        "description": "API related issues",
        "type": "ProjectLabel",
        "group_id": 41
      }]
  },
  "repository": {
    "name": "Gitlab Test",
    "url": "http://example.com/gitlabhq/gitlab-test.git",
    "description": "Aut reprehenderit ut est.",
    "homepage": "http://example.com/gitlabhq/gitlab-test"
  },
  "assignees": [{
    "name": "User1",
    "username": "user1",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
  }],
  "assignee": {
    "name": "User1",
    "username": "user1",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
  },
  "labels": [{
    "id": 206,
    "title": "API",
    "color": "#ffffff",
    "project_id": 14,
    "created_at": "2013-12-03T17:15:43Z",
    "updated_at": "2013-12-03T17:15:43Z",
    "template": false,
    "description": "API related issues",
    "type": "ProjectLabel",
    "group_id": 41
  }],
  "changes": {
    "updated_by_id": {
      "previous": null,
      "current": 1
    },
    "updated_at": {
      "previous": "2017-09-15 16:50:55 UTC",
      "current": "2017-09-15 16:52:00 UTC"
    },
    "labels": {
      "previous": [{
        "id": 206,
        "title": "API",
        "color": "#ffffff",
        "project_id": 14,
        "created_at": "2013-12-03T17:15:43Z",
        "updated_at": "2013-12-03T17:15:43Z",
        "template": false,
        "description": "API related issues",
        "type": "ProjectLabel",
        "group_id": 41
      }],
      "current": [{
        "id": 205,
        "title": "Platform",
        "color": "#123123",
        "project_id": 14,
        "created_at": "2013-12-03T17:15:43Z",
        "updated_at": "2013-12-03T17:15:43Z",
        "template": false,
        "description": "Platform related issues",
        "type": "ProjectLabel",
        "group_id": 41
      }]
    }
  }
}
```

## 댓글 이벤트

댓글 이벤트는 커밋, 머지 리퀘스트, 이슈 및 코드 스니펫에 새 댓글이 작성되거나 편집될 때 트리거됩니다.

노트 데이터는 `object_attributes`에 저장됩니다(예: `note` 또는 `noteable_type`). 페이로드에는 댓글 대상에 대한 정보가 포함됩니다. 예를 들어, 이슈에 대한 댓글에는 `issue` 키 아래에 특정 이슈 정보가 포함됩니다.

사용 가능한 대상 유형:

- `commit`
- `merge_request`
- `issue`
- `snippet`

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `create`
- `update`

### 커밋에 대한 댓글

요청 헤더:

```plaintext
X-Gitlab-Event: Note Hook
```

페이로드 예제:

```json
{
  "object_kind": "note",
  "event_type": "note",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project_id": 5,
  "project":{
    "id": 5,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlabhq/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "git_http_url":"http://example.com/gitlabhq/gitlab-test.git",
    "namespace":"GitlabHQ",
    "visibility_level":20,
    "path_with_namespace":"gitlabhq/gitlab-test",
    "default_branch":"master",
    "homepage":"http://example.com/gitlabhq/gitlab-test",
    "url":"http://example.com/gitlabhq/gitlab-test.git",
    "ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "http_url":"http://example.com/gitlabhq/gitlab-test.git"
  },
  "repository":{
    "name": "Gitlab Test",
    "url": "http://example.com/gitlab-org/gitlab-test.git",
    "description": "Aut reprehenderit ut est.",
    "homepage": "http://example.com/gitlab-org/gitlab-test"
  },
  "object_attributes": {
    "id": 1243,
    "internal": false,
    "note": "This is a commit comment. How does this work?",
    "noteable_type": "Commit",
    "author_id": 1,
    "created_at": "2015-05-17 18:08:09 UTC",
    "updated_at": "2015-05-17 18:08:09 UTC",
    "project_id": 5,
    "attachment":null,
    "line_code": "bec9703f7a456cd2b4ab5fb3220ae016e3e394e3_0_1",
    "commit_id": "cfe32cf61b73a0d5e9f13e774abde7ff789b1660",
    "noteable_id": null,
    "system": false,
    "st_diff": {
      "diff": "--- /dev/null\n+++ b/six\n@@ -0,0 +1 @@\n+Subproject commit 409f37c4f05865e4fb208c771485f211a22c4c2d\n",
      "new_path": "six",
      "old_path": "six",
      "a_mode": "0",
      "b_mode": "160000",
      "new_file": true,
      "renamed_file": false,
      "deleted_file": false
    },
    "action": "create",
    "url": "http://example.com/gitlab-org/gitlab-test/commit/cfe32cf61b73a0d5e9f13e774abde7ff789b1660#note_1243"
  },
  "commit": {
    "id": "cfe32cf61b73a0d5e9f13e774abde7ff789b1660",
    "message": "Add submodule\n\nSigned-off-by: Example User \u003cuser@example.com.com\u003e\n",
    "timestamp": "2014-02-27T10:06:20+02:00",
    "url": "http://example.com/gitlab-org/gitlab-test/commit/cfe32cf61b73a0d5e9f13e774abde7ff789b1660",
    "author": {
      "name": "Example User",
      "email": "user@example.com"
    }
  }
}
```

### 머지 리퀘스트에 대한 댓글

요청 헤더:

```plaintext
X-Gitlab-Event: Note Hook
```

페이로드 예제:

```json
{
  "object_kind": "note",
  "event_type": "note",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project_id": 5,
  "project":{
    "id": 5,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlab-org/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "git_http_url":"http://example.com/gitlab-org/gitlab-test.git",
    "namespace":"Gitlab Org",
    "visibility_level":10,
    "path_with_namespace":"gitlab-org/gitlab-test",
    "default_branch":"master",
    "homepage":"http://example.com/gitlab-org/gitlab-test",
    "url":"http://example.com/gitlab-org/gitlab-test.git",
    "ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "http_url":"http://example.com/gitlab-org/gitlab-test.git"
  },
  "repository":{
    "name": "Gitlab Test",
    "url": "http://localhost/gitlab-org/gitlab-test.git",
    "description": "Aut reprehenderit ut est.",
    "homepage": "http://example.com/gitlab-org/gitlab-test"
  },
  "object_attributes": {
    "id": 1244,
    "internal": false,
    "note": "This MR needs work.",
    "noteable_type": "MergeRequest",
    "author_id": 1,
    "created_at": "2015-05-17 18:21:36 UTC",
    "updated_at": "2015-05-17 18:21:36 UTC",
    "project_id": 5,
    "attachment": null,
    "line_code": null,
    "commit_id": "",
    "noteable_id": 7,
    "system": false,
    "st_diff": null,
    "action": "create",
    "url": "http://example.com/gitlab-org/gitlab-test/merge_requests/1#note_1244"
  },
  "merge_request": {
    "id": 7,
    "target_branch": "markdown",
    "source_branch": "master",
    "source_project_id": 5,
    "author_id": 8,
    "assignee_id": 28,
    "title": "Tempora et eos debitis quae laborum et.",
    "created_at": "2015-03-01 20:12:53 UTC",
    "updated_at": "2015-03-21 18:27:27 UTC",
    "milestone_id": 11,
    "state": "opened",
    "merge_status": "cannot_be_merged",
    "target_project_id": 5,
    "iid": 1,
    "description": "Et voluptas corrupti assumenda temporibus. Architecto cum animi eveniet amet asperiores. Vitae numquam voluptate est natus sit et ad id.",
    "position": 0,
    "labels": [
      {
        "id": 25,
        "title": "Afterpod",
        "color": "#3e8068",
        "project_id": null,
        "created_at": "2019-06-05T14:32:20.211Z",
        "updated_at": "2019-06-05T14:32:20.211Z",
        "template": false,
        "description": null,
        "type": "GroupLabel",
        "group_id": 4
      },
      {
        "id": 86,
        "title": "Element",
        "color": "#231afe",
        "project_id": 4,
        "created_at": "2019-06-05T14:32:20.637Z",
        "updated_at": "2019-06-05T14:32:20.637Z",
        "template": false,
        "description": null,
        "type": "ProjectLabel",
        "group_id": null
      }
    ],
    "source":{
      "name":"Gitlab Test",
      "description":"Aut reprehenderit ut est.",
      "web_url":"http://example.com/gitlab-org/gitlab-test",
      "avatar_url":null,
      "git_ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
      "git_http_url":"http://example.com/gitlab-org/gitlab-test.git",
      "namespace":"Gitlab Org",
      "visibility_level":10,
      "path_with_namespace":"gitlab-org/gitlab-test",
      "default_branch":"master",
      "homepage":"http://example.com/gitlab-org/gitlab-test",
      "url":"http://example.com/gitlab-org/gitlab-test.git",
      "ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
      "http_url":"http://example.com/gitlab-org/gitlab-test.git"
    },
    "target": {
      "name":"Gitlab Test",
      "description":"Aut reprehenderit ut est.",
      "web_url":"http://example.com/gitlab-org/gitlab-test",
      "avatar_url":null,
      "git_ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
      "git_http_url":"http://example.com/gitlab-org/gitlab-test.git",
      "namespace":"Gitlab Org",
      "visibility_level":10,
      "path_with_namespace":"gitlab-org/gitlab-test",
      "default_branch":"master",
      "homepage":"http://example.com/gitlab-org/gitlab-test",
      "url":"http://example.com/gitlab-org/gitlab-test.git",
      "ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
      "http_url":"http://example.com/gitlab-org/gitlab-test.git"
    },
    "last_commit": {
      "id": "562e173be03b8ff2efb05345d12df18815438a4b",
      "message": "Merge branch 'another-branch' into 'master'\n\nCheck in this test\n",
      "timestamp": "2015-04-08T21: 00:25-07:00",
      "url": "http://example.com/gitlab-org/gitlab-test/commit/562e173be03b8ff2efb05345d12df18815438a4b",
      "author": {
        "name": "John Smith",
        "email": "john@example.com"
      }
    },
    "work_in_progress": false,
    "draft": false,
    "assignee": {
      "name": "User1",
      "username": "user1",
      "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
    },
    "detailed_merge_status": "checking"
  }
}
```

### 이슈에 대한 댓글

- `assignee_id` 필드는 더 이상 사용되지 않으며 첫 번째 담당자만 표시합니다.
- 기밀 이슈의 경우 `event_type`이 `confidential_note`로 설정됩니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Note Hook
```

페이로드 예제:

```json
{
  "object_kind": "note",
  "event_type": "note",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project_id": 5,
  "project":{
    "id": 5,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlab-org/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "git_http_url":"http://example.com/gitlab-org/gitlab-test.git",
    "namespace":"Gitlab Org",
    "visibility_level":10,
    "path_with_namespace":"gitlab-org/gitlab-test",
    "default_branch":"master",
    "homepage":"http://example.com/gitlab-org/gitlab-test",
    "url":"http://example.com/gitlab-org/gitlab-test.git",
    "ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "http_url":"http://example.com/gitlab-org/gitlab-test.git"
  },
  "repository":{
    "name":"diaspora",
    "url":"git@example.com:mike/diaspora.git",
    "description":"",
    "homepage":"http://example.com/mike/diaspora"
  },
  "object_attributes": {
    "id": 1241,
    "internal": false,
    "note": "Hello world",
    "noteable_type": "Issue",
    "author_id": 1,
    "created_at": "2015-05-17 17:06:40 UTC",
    "updated_at": "2015-05-17 17:06:40 UTC",
    "project_id": 5,
    "attachment": null,
    "line_code": null,
    "commit_id": "",
    "noteable_id": 92,
    "system": false,
    "st_diff": null,
    "action": "create",
    "url": "http://example.com/gitlab-org/gitlab-test/issues/17#note_1241"
  },
  "issue": {
    "id": 92,
    "title": "test",
    "assignee_ids": [],
    "assignee_id": null,
    "author_id": 1,
    "project_id": 5,
    "created_at": "2015-04-12 14:53:17 UTC",
    "updated_at": "2015-04-26 08:28:42 UTC",
    "position": 0,
    "branch_name": null,
    "description": "test",
    "milestone_id": null,
    "state": "closed",
    "iid": 17,
    "labels": [
      {
        "id": 25,
        "title": "Afterpod",
        "color": "#3e8068",
        "project_id": null,
        "created_at": "2019-06-05T14:32:20.211Z",
        "updated_at": "2019-06-05T14:32:20.211Z",
        "template": false,
        "description": null,
        "type": "GroupLabel",
        "group_id": 4
      },
      {
        "id": 86,
        "title": "Element",
        "color": "#231afe",
        "project_id": 4,
        "created_at": "2019-06-05T14:32:20.637Z",
        "updated_at": "2019-06-05T14:32:20.637Z",
        "template": false,
        "description": null,
        "type": "ProjectLabel",
        "group_id": null
      }
    ]
  }
}
```

### 코드 스니펫에 대한 댓글

요청 헤더:

```plaintext
X-Gitlab-Event: Note Hook
```

페이로드 예제:

```json
{
  "object_kind": "note",
  "event_type": "note",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project_id": 5,
  "project":{
    "id": 5,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlab-org/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "git_http_url":"http://example.com/gitlab-org/gitlab-test.git",
    "namespace":"Gitlab Org",
    "visibility_level":10,
    "path_with_namespace":"gitlab-org/gitlab-test",
    "default_branch":"master",
    "homepage":"http://example.com/gitlab-org/gitlab-test",
    "url":"http://example.com/gitlab-org/gitlab-test.git",
    "ssh_url":"git@example.com:gitlab-org/gitlab-test.git",
    "http_url":"http://example.com/gitlab-org/gitlab-test.git"
  },
  "repository":{
    "name":"Gitlab Test",
    "url":"http://example.com/gitlab-org/gitlab-test.git",
    "description":"Aut reprehenderit ut est.",
    "homepage":"http://example.com/gitlab-org/gitlab-test"
  },
  "object_attributes": {
    "id": 1245,
    "internal": false,
    "note": "Is this snippet doing what it's supposed to be doing?",
    "noteable_type": "Snippet",
    "author_id": 1,
    "created_at": "2015-05-17 18:35:50 UTC",
    "updated_at": "2015-05-17 18:35:50 UTC",
    "project_id": 5,
    "attachment": null,
    "line_code": null,
    "commit_id": "",
    "noteable_id": 53,
    "system": false,
    "st_diff": null,
    "action": "create",
    "url": "http://example.com/gitlab-org/gitlab-test/-/snippets/53#note_1245"
  },
  "snippet": {
    "id": 53,
    "title": "test",
    "description": "A snippet description.",
    "content": "puts 'Hello world'",
    "author_id": 1,
    "project_id": 5,
    "created_at": "2015-04-09 02:40:38 UTC",
    "updated_at": "2015-04-09 02:40:38 UTC",
    "file_name": "test.rb",
    "type": "ProjectSnippet",
    "visibility_level": 0,
    "url": "http://example.com/gitlab-org/gitlab-test/-/snippets/53"
  }
}
```

## 머지 리퀘스트 이벤트

머지 리퀘스트 이벤트는 다음과 같은 경우에 트리거됩니다:

- 새 머지 리퀘스트가 생성됨
- 기존 머지 리퀘스트가 업데이트, 승인(모든 필수 승인자에 의해), 승인 취소, 병합 또는 종료됨
- 개별 사용자가 기존 머지 리퀘스트에 대한 승인을 추가하거나 제거함
- 리뷰어에게 머지 리퀘스트 리뷰가 다시 요청됨
- 머지 리퀘스트가 자동 병합으로 설정되거나 자동 병합이 취소됨
- 소스 브랜치에 커밋이 추가됨
- 머지 리퀘스트의 모든 스레드가 해결됨

`changes` 필드가 비어 있더라도 머지 리퀘스트 이벤트가 트리거될 수 있습니다. 웹훅 수신기는 머지 리퀘스트의 실제 변경 사항을 위해 항상 `changes` 필드의 내용을 검사해야 합니다.

### 페이로드 구조

웹훅 페이로드의 JSON 구조는 모든 액션 유형에서 일관됩니다. 차이점은 어떤 필드에 데이터가 포함되는지와 `oldrev`, `system`, `system_action`과 같은 조건부 필드의 존재 여부입니다.

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `open`: 머지 리퀘스트가 생성됨
- `close`: 머지 리퀘스트가 종료됨
- `reopen`: 종료된 머지 리퀘스트가 재개됨
- `update`: 머지 리퀘스트가 업데이트됨. 일반 업데이트, 리뷰 재요청, 자동 병합 설정 또는 취소를 포함합니다. 특정 업데이트 유형을 확인하려면 `changes` 필드를 확인하세요. 자동 병합이 설정되거나 취소되면 `changes` 필드는 머지 리퀘스트의 자동 병합 상태 변경을 반영합니다.
- `approval`: 사용자가 승인을 추가함
- `approved`: 모든 필수 승인자에 의해 머지 리퀘스트가 완전히 승인됨
- `unapproval`: 사용자가 수동 또는 시스템에 의해 승인을 제거함
- `unapproved`: 이전에 승인된 머지 리퀘스트가 수동 또는 시스템에 의해 승인 상태를 상실함
- `merge`: 머지 리퀘스트가 병합됨

머지 리퀘스트 웹훅 페이로드에는 다음 최상위 필드가 포함됩니다:

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `object_kind` | 문자열 | `"merge_request"` |
| `event_type` | 문자열 | `"merge_request"` |
| `user` | 객체 | 이벤트를 트리거한 사용자 |
| `project` | 객체 | 대상 프로젝트 |
| `object_attributes` | 객체 | 머지 리퀘스트 데이터 |
| `changes` | 객체 | 액션 중 변경된 속성 포함 |
| `assignees` | 배열 | 현재 할당된 사용자 |
| `reviewers` | 배열 | 현재 할당된 리뷰어 |
| `labels` | 배열 | 레이블 객체 |
| `repository` | 객체 | 더 이상 사용되지 않음. `project`를 대신 사용. 리포지토리 정보 |

### 더 이상 사용되지 않는 필드

다음 필드는 더 이상 사용되지 않으며 이전 버전과의 호환성을 위해서만 포함됩니다. 대신 권장 대체 필드를 사용하세요:

| 더 이상 사용되지 않는 필드 | 권장 대체 필드 |
| --- | --- |
| `object_attributes.assignee_id` | `object_attributes.assignee_ids` |
| `object_attributes.work_in_progress` | `object_attributes.draft` |
| `project.http_url` | `project.git_http_url` |
| `project.homepage` | `project.web_url` |
| `project.ssh_url` | `project.git_ssh_url` |
| `project.url` | `project.git_ssh_url` 또는 `project.git_http_url` |
| `repository` | `project` |

### object\_attributes 필드

`object_attributes` 필드에는 머지 리퀘스트의 현재 상태가 포함됩니다. 다음 필드가 포함됩니다:

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `action` | 문자열 | 웹훅을 트리거한 액션 (예: `open`, `update`, `merge`) |
| `actioned_at` | 문자열 | 웹훅을 트리거한 액션이 발생한 시간 |
| `approval_rules` | 배열 | 승인 규칙 객체 배열 (EE 전용) |
| `assignee_ids` | 배열 | 담당자 ID 배열 |
| `author_id` | 정수 | 머지 리퀘스트 작성자 ID |
| `blocking_discussions_resolved` | 불리언 | 차단 토론이 해결되었는지 여부 |
| `created_at` | 문자열 | 머지 리퀘스트가 생성된 시간 |
| `description` | 문자열 | 머지 리퀘스트 설명 |
| `detailed_merge_status` | 문자열 | 상세 병합 상태 정보. 가능한 값 목록은 [병합 상태](https://docs.gitlab.com/api/merge_requests/#merge-status) 참조 |
| `draft` | 불리언 | 머지 리퀘스트가 초안인지 여부 |
| `first_contribution` | 불리언 | 작성자의 첫 번째 기여인지 여부 |
| `head_pipeline_id` | 정수 | 헤드 파이프라인 ID |
| `human_time_change` | 문자열 | 사람이 읽을 수 있는 시간 변경 |
| `human_time_estimate` | 문자열 | 사람이 읽을 수 있는 시간 추정 |
| `human_total_time_spent` | 문자열 | 사람이 읽을 수 있는 총 소요 시간 |
| `id` | 정수 | 머지 리퀘스트 ID |
| `iid` | 정수 | 머지 리퀘스트의 내부 ID |
| `labels` | 배열 | 레이블 객체 배열 |
| `last_commit` | 객체 | 세부 정보가 포함된 마지막 커밋 객체 |
| `last_edited_at` | 문자열 | 머지 리퀘스트가 마지막으로 편집된 시간 |
| `last_edited_by_id` | 정수 | 마지막으로 편집한 사용자 ID |
| `merge_commit_sha` | 문자열 | 병합 커밋의 SHA |
| `merged_at` | 문자열 | 머지 리퀘스트가 병합된 시간. 아직 병합되지 않은 경우 `null` |
| `merge_error` | 문자열 | 병합 오류 메시지 |
| `merge_params` | 객체 | 병합 매개변수 |
| `merge_status` | 문자열 | 머지 리퀘스트의 상태 |
| `merge_user_id` | 정수 | 병합한 사용자 ID |
| `merge_when_pipeline_succeeds` | 불리언 | 자동 병합이 활성화되었는지 여부 |
| `milestone_id` | 정수 | 마일스톤 ID |
| `oldrev` | 문자열 | 이전 커밋 SHA (푸시 관련 이벤트에만 존재) |
| `prepared_at` | 문자열 | 머지 리퀘스트가 준비된 타임스탬프. 이 필드는 모든 [준비 단계](https://docs.gitlab.com/api/merge_requests/#preparation-steps)가 완료된 후 한 번만 채워지며, 추가 변경 사항이 추가되어도 업데이트되지 않음 |
| `reviewer_ids` | 배열 | 리뷰어 ID 배열 |
| `source_branch` | 문자열 | 소스 브랜치 이름 |
| `source` | 객체 | 소스 프로젝트 세부 정보 (이름, 설명 등) |
| `source_project_id` | 정수 | 소스 프로젝트 ID |
| `squash_commit_sha` | 문자열 | 스쿼시 커밋의 SHA. 머지 리퀘스트가 스쿼시와 함께 병합된 경우에만 존재 |
| `state_id` | 정수 | 상태 ID (`1`: opened, `2`: closed, `3`: merged, `4`: locked) |
| `state` | 문자열 | 머지 리퀘스트의 상태 (`opened`, `closed`, `merged`, `locked`) |
| `system_action` | 문자열 | 시스템 액션 (`system`이 `true`인 경우에만 존재) |
| `system` | 불리언 | 이벤트가 시스템에 의해 시작되었는지 여부 |
| `target_branch` | 문자열 | 대상 브랜치 이름 |
| `target_branch_protected` | 불리언 | 대상 브랜치가 [보호된 브랜치](https://docs.gitlab.com/user/project/repository/branches/protected/)인지 여부 |
| `target` | 객체 | 대상 프로젝트 세부 정보 (이름, 설명 등) |
| `target_project_id` | 정수 | 대상 프로젝트 ID |
| `time_change` | 정수 | 초 단위 시간 변경 |
| `time_estimate` | 정수 | 초 단위 시간 추정 |
| `title` | 문자열 | 머지 리퀘스트 제목 |
| `total_time_spent` | 정수 | 초 단위 총 소요 시간 |
| `updated_at` | 문자열 | 머지 리퀘스트가 마지막으로 업데이트된 시간 |
| `updated_by_id` | 정수 | 마지막으로 업데이트한 사용자 ID |
| `url` | 문자열 | 머지 리퀘스트 URL |

### changes 필드

`changes` 필드에는 액션 중 수정된 필드만 포함됩니다. `object_attributes`의 모든 필드가 `changes`에 나타나는 것은 아닙니다.

각 변경된 필드는 다음 형식을 따릅니다:

```json
{
  "field_name": {
    "previous": "old_value",
    "current": "new_value"
  }
}
```

#### 속성

- `assignees`
- `blocking_discussions_resolved`
- `description`
- `draft`
- `head_pipeline_id`
- `labels`
- `last_edited_at`
- `last_edited_by_id`
- `merge_commit_sha`
- `merge_error`
- `merge_params`
- `merge_status`
- `merge_user_id`
- `merge_when_pipeline_succeeds`
- `milestone_id`
- `prepared_at`
- `reviewer_ids`
- `reviewers`
- `squash_commit_sha`
- `state_id`
- `target_branch`
- `time_change`
- `time_estimate`
- `title`
- `total_time_spent`
- `updated_at`
- `updated_by_id`

### 머지 리퀘스트 액션별 필드

`object_attributes.oldrev` 필드는 실제 코드 변경이 있을 때만 `update` 액션에 사용할 수 있습니다. 예:

- 소스 브랜치에 새 코드가 푸시됨
- [제안(suggestion)](https://docs.gitlab.com/user/project/merge_requests/reviews/suggestions/)이 적용됨

다음 예제는 `oldrev`가 포함된 `update` 이벤트를 보여줍니다 (부분 페이로드):

```json
{
  "object_kind": "merge_request",
  "event_type": "merge_request",
  "object_attributes": {
    "action": "update",
    "oldrev": "e59094b8de0f2f91abbe4760a52d9137260252d8"
  }
}
```

### 시스템 시작 머지 리퀘스트 이벤트

일부 머지 리퀘스트 이벤트는 새 커밋 푸시로 인한 승인 재설정과 같이 시스템에 의해 자동으로 트리거됩니다. 이러한 시스템 시작 웹훅 이벤트는 푸시 이벤트에 의해서만 트리거되며 페이로드에 더 많은 필드가 포함됩니다:

- `object_attributes.system`: 불리언 필드. `true`인 경우 시스템에 의해 이벤트가 트리거됨. `false`인 경우 사용자 액션에 의해 트리거됨.
- `object_attributes.system_action`: 문자열 필드, `system`이 `true`인 경우에만 존재. 시스템 액션에 대한 추가 컨텍스트 제공. 사용 가능한 값:
  - `approvals_reset_on_push`: 프로젝트에서 **Reset approvals on push**가 활성화되어 있고 새 커밋이 푸시됨
  - `code_owner_approvals_reset_on_push`: 프로젝트에서 **Selective code owner removals**가 활성화되어 있고 CODEOWNERS 규칙과 일치하는 파일 변경으로 인해 Code Owner 승인이 재설정됨
- `object_attributes.action`: 승인 재설정 이벤트의 경우 값:
  - 머지 리퀘스트가 승인됨에서 승인되지 않음으로 변경되면 `unapproved`
  - 전체 승인 상태를 변경하지 않고 승인이 제거되면 `unapproval`

다른 승인 재설정 시나리오는 웹훅을 트리거하지 않습니다.

다음 예제는 시스템 시작 이벤트를 보여줍니다 (부분 페이로드):

```json
{
  "object_kind": "merge_request",
  "event_type": "merge_request",
  "object_attributes": {
    "action": "unapproved",
    "system": true,
    "system_action": "approvals_reset_on_push"
  }
}
```

### 리뷰어 상태 추적

머지 리퀘스트 웹훅 페이로드의 `reviewers` 배열에는 각 리뷰어에 대한 `state` 필드가 포함됩니다. `state` 필드는 리뷰어의 현재 리뷰 상태를 나타냅니다:

- `unreviewed`: 리뷰어가 아직 머지 리퀘스트를 리뷰하지 않음
- `review_started`: 리뷰어가 리뷰를 시작했지만 완료하지 않음
- `reviewed`: 리뷰어가 리뷰를 완료함
- `requested_changes`: 리뷰어가 변경을 요청함
- `approved`: 리뷰어가 머지 리퀘스트를 승인함
- `unapproved`: 리뷰어가 이전에 승인했지만 승인이 제거됨

다음 예제는 리뷰어 배열을 보여줍니다 (부분 페이로드):

```json
{
  "reviewers": [
    {
      "id": 6,
      "name": "User1",
      "username": "user1",
      "state": "unreviewed",
      "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
      "email": "user1@example.com"
    }
  ]
}
```

### 리뷰 재요청 이벤트

머지 리퀘스트에 대해 리뷰어에게 재요청이 되면 `action: "update"`로 웹훅이 트리거되며, `changes` 객체에 향상된 정보가 포함됩니다. changes 페이로드에는 다음이 포함됩니다:

- **이전 상태** (첫 번째 배열): 재요청 전 리뷰어의 상태, `re_requested: false`로 표시
- **현재 상태** (두 번째 배열): 재요청 후 리뷰어의 업데이트된 상태, 재요청된 리뷰어에 대해 `re_requested: true`로 표시
- **상태 전환**: 리뷰어의 상태가 어떻게 변경되었는지 보여줌 (예: `approved`에서 `unreviewed`로)

다음 예제는 리뷰 재요청 변경 사항을 보여줍니다 (부분 페이로드):

```json
{
  "object_kind": "merge_request",
  "event_type": "merge_request",
  "object_attributes": {
    "action": "update"
  },
  "changes": {
    "reviewers": [
      [
        {
          "id": 6,
          "name": "User1",
          "username": "user1",
          "state": "approved",
          "re_requested": false,
          "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
          "email": "user1@example.com"
        }
      ],
      [
        {
          "id": 6,
          "name": "User1",
          "username": "user1",
          "state": "unreviewed",
          "re_requested": true,
          "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
          "email": "user1@example.com"
        }
      ]
    ]
  }
}
```

### 전체 페이로드 예제

요청 헤더:

```plaintext
X-Gitlab-Event: Merge Request Hook
```

다음 예제는 `open` 액션에 대한 완전한 머지 리퀘스트 웹훅 페이로드입니다. 더 이상 사용되지 않는 필드는 명확성을 위해 생략되었습니다. 더 이상 사용되지 않는 필드 및 권장 대체 필드 목록은 [더 이상 사용되지 않는 필드](https://docs.gitlab.com/user/project/integrations/webhook_events/#deprecated-fields)를 참조하세요.

```json
{
  "object_kind": "merge_request",
  "event_type": "merge_request",
  "user": {
    "id": 1,
    "name": "Alex Garcia",
    "username": "agarcia",
    "avatar_url": "https://www.gravatar.com/avatar/1a29da0ccd099482194440fac762f5ccb4ec53227761d1859979367644a889a5?s=80&d=identicon",
    "email": "agarcia@example.com"
  },
  "project": {
    "id": 2,
    "name": "Flight Management",
    "description": "Flight management application for tracking aircraft status.",
    "web_url": "http://gitlab.example.com/flightjs/flight-management",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@gitlab.example.com:flightjs/flight-management.git",
    "git_http_url": "http://gitlab.example.com/flightjs/flight-management.git",
    "namespace": "Flightjs",
    "visibility_level": 0,
    "path_with_namespace": "flightjs/flight-management",
    "default_branch": "main",
    "ci_config_path": null
  },
  "object_attributes": {
    "author_id": 1,
    "created_at": "2026-01-16 05:56:22 UTC",
    "description": "This merge request adds input validation to the booking form.",
    "draft": false,
    "head_pipeline_id": null,
    "id": 93,
    "iid": 16,
    "last_edited_at": null,
    "last_edited_by_id": null,
    "merge_commit_sha": null,
    "merged_at": null,
    "merge_error": null,
    "merge_params": {
      "force_remove_source_branch": "1"
    },
    "merge_status": "checking",
    "merge_user_id": null,
    "merge_when_pipeline_succeeds": false,
    "milestone_id": 8,
    "source_branch": "feature/booking-validation",
    "source_project_id": 2,
    "squash_commit_sha": null,
    "state_id": 1,
    "target_branch": "main",
    "target_branch_protected": true,
    "target_project_id": 2,
    "time_estimate": 0,
    "title": "Add input validation to booking form",
    "updated_at": "2026-01-16 05:56:25 UTC",
    "updated_by_id": null,
    "prepared_at": "2026-01-16 05:56:25 UTC",
    "assignee_ids": [
      1
    ],
    "blocking_discussions_resolved": true,
    "detailed_merge_status": "checking",
    "first_contribution": true,
    "human_time_change": null,
    "human_time_estimate": null,
    "human_total_time_spent": null,
    "labels": [
      {
        "id": 19,
        "title": "enhancement",
        "color": "#adb21a",
        "project_id": null,
        "created_at": "2026-01-07 00:03:52 UTC",
        "updated_at": "2026-01-07 00:03:52 UTC",
        "template": false,
        "description": null,
        "type": "GroupLabel",
        "group_id": 24
      }
    ],
    "last_commit": {
      "id": "e59094b8de0f2f91abbe4760a52d9137260252d8",
      "message": "Add email format validation",
      "title": "Add email format validation",
      "timestamp": "2026-01-16T05:01:10+00:00",
      "url": "http://gitlab.example.com/flightjs/flight-management/-/commit/e59094b8de0f2f91abbe4760a52d9137260252d8",
      "author": {
        "name": "Alex Garcia",
        "email": "agarcia@example.com"
      }
    },
    "reviewer_ids": [
      25
    ],
    "source": {
      "id": 2,
      "name": "Flight Management",
      "description": "Flight management application for tracking aircraft status.",
      "web_url": "http://gitlab.example.com/flightjs/flight-management",
      "avatar_url": null,
      "git_ssh_url": "ssh://git@gitlab.example.com:flightjs/flight-management.git",
      "git_http_url": "http://gitlab.example.com/flightjs/flight-management.git",
      "namespace": "Flightjs",
      "visibility_level": 0,
      "path_with_namespace": "flightjs/flight-management",
      "default_branch": "main",
      "ci_config_path": null
    },
    "state": "opened",
    "system": false,
    "target": {
      "id": 2,
      "name": "Flight Management",
      "description": "Flight management application for tracking aircraft status.",
      "web_url": "http://gitlab.example.com/flightjs/flight-management",
      "avatar_url": null,
      "git_ssh_url": "ssh://git@gitlab.example.com:flightjs/flight-management.git",
      "git_http_url": "http://gitlab.example.com/flightjs/flight-management.git",
      "namespace": "Flightjs",
      "visibility_level": 0,
      "path_with_namespace": "flightjs/flight-management",
      "default_branch": "main",
      "ci_config_path": null
    },
    "time_change": 0,
    "total_time_spent": 0,
    "url": "http://gitlab.example.com/flightjs/flight-management/-/merge_requests/16",
    "approval_rules": [
      {
        "id": 4,
        "approvals_required": 0,
        "name": "All Members",
        "rule_type": "any_approver",
        "report_type": null,
        "merge_request_id": 93,
        "section": null,
        "modified_from_project_rule": false,
        "orchestration_policy_idx": null,
        "vulnerabilities_allowed": 0,
        "scanners": [],
        "severity_levels": [],
        "vulnerability_states": [
          "new_needs_triage",
          "new_dismissed"
        ],
        "security_orchestration_policy_configuration_id": null,
        "scan_result_policy_id": null,
        "applicable_post_merge": null,
        "project_id": 2,
        "approval_policy_rule_id": null,
        "updated_at": "2026-01-16 05:56:22 UTC",
        "created_at": "2026-01-16 05:56:22 UTC"
      }
    ],
    "action": "open",
    "actioned_at": "2026-01-16 05:56:26 UTC"
  },
  "labels": [
    {
      "id": 19,
      "title": "enhancement",
      "color": "#adb21a",
      "project_id": null,
      "created_at": "2026-01-07 00:03:52 UTC",
      "updated_at": "2026-01-07 00:03:52 UTC",
      "template": false,
      "description": null,
      "type": "GroupLabel",
      "group_id": 24
    }
  ],
  "changes": {
    "merge_status": {
      "previous": "preparing",
      "current": "checking"
    },
    "updated_at": {
      "previous": "2026-01-16 05:56:22 UTC",
      "current": "2026-01-16 05:56:25 UTC"
    },
    "prepared_at": {
      "previous": null,
      "current": "2026-01-16 05:56:25 UTC"
    }
  },
  "assignees": [
    {
      "id": 1,
      "name": "Alex Garcia",
      "username": "agarcia",
      "avatar_url": "https://www.gravatar.com/avatar/1a29da0ccd099482194440fac762f5ccb4ec53227761d1859979367644a889a5?s=80&d=identicon",
      "email": "[REDACTED]"
    }
  ],
  "reviewers": [
    {
      "id": 25,
      "name": "Sidney Jones",
      "username": "sjones",
      "avatar_url": "https://www.gravatar.com/avatar/1be419860e7f852e20ca2691e6b55949f7809177e7765181da42e4448491e367?s=80&d=identicon",
      "email": "[REDACTED]",
      "state": "unreviewed",
      "re_requested": false
    }
  ]
}
```

> [!type-note] 유형 노트
> `assignee_id` 및 `merge_status` 필드는 [더 이상 사용되지 않습니다](https://docs.gitlab.com/api/merge_requests/).

## 위키 페이지 이벤트

위키 페이지 이벤트는 위키 페이지가 생성, 업데이트 또는 삭제될 때 트리거됩니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Wiki Page Hook
```

페이로드 예제:

```json
{
  "object_kind": "wiki_page",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80\u0026d=identicon",
    "email": "admin@example.com"
  },
  "project": {
    "id": 1,
    "name": "awesome-project",
    "description": "This is awesome",
    "web_url": "http://example.com/root/awesome-project",
    "avatar_url": null,
    "git_ssh_url": "git@example.com:root/awesome-project.git",
    "git_http_url": "http://example.com/root/awesome-project.git",
    "namespace": "root",
    "visibility_level": 0,
    "path_with_namespace": "root/awesome-project",
    "default_branch": "master",
    "homepage": "http://example.com/root/awesome-project",
    "url": "git@example.com:root/awesome-project.git",
    "ssh_url": "git@example.com:root/awesome-project.git",
    "http_url": "http://example.com/root/awesome-project.git"
  },
  "wiki": {
    "web_url": "http://example.com/root/awesome-project/-/wikis/home",
    "git_ssh_url": "git@example.com:root/awesome-project.wiki.git",
    "git_http_url": "http://example.com/root/awesome-project.wiki.git",
    "path_with_namespace": "root/awesome-project.wiki",
    "default_branch": "master"
  },
  "object_attributes": {
    "title": "Awesome",
    "content": "awesome content goes here",
    "format": "markdown",
    "message": "adding an awesome page to the wiki",
    "slug": "awesome",
    "url": "http://example.com/root/awesome-project/-/wikis/awesome",
    "action": "create",
    "diff_url": "http://example.com/root/awesome-project/-/wikis/home/diff?version_id=78ee4a6705abfbff4f4132c6646dbaae9c8fb6ec",
    "version_id": "3ad67c972065298d226dd80b2b03e0fc2421e731"
  }
}
```

## 파이프라인 이벤트

파이프라인 이벤트는 파이프라인의 상태가 변경될 때 트리거됩니다.

GitLab 15.1 이상에서 차단된 사용자가 트리거한 파이프라인 웹훅은 처리되지 않습니다.

GitLab 16.1 이상에서 파이프라인 웹훅은 `object_attributes.name`을 노출하기 시작했습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Pipeline Hook
```

페이로드 예제:

```json
{
  "object_kind": "pipeline",
  "object_attributes": {
    "id": 31,
    "iid": 3,
    "name": "Pipeline for branch: master",
    "ref": "master",
    "tag": false,
    "sha": "bcbb5ec396a2c0f828686f14fac9b80b780504f2",
    "before_sha": "bcbb5ec396a2c0f828686f14fac9b80b780504f2",
    "source": "merge_request_event",
    "status": "success",
    "detailed_status": "passed",
    "stages": [
      "build",
      "test",
      "deploy"
    ],
    "created_at": "2016-08-12 15:23:28 UTC",
    "finished_at": "2016-08-12 15:26:29 UTC",
    "duration": 63,
    "queued_duration": 10,
    "variables": [
      {
        "key": "NESTOR_PROD_ENVIRONMENT",
        "value": "us-west-1"
      }
    ],
    "url": "http://example.com/gitlab-org/gitlab-test/-/pipelines/31"
  },
  "merge_request": {
    "id": 1,
    "iid": 1,
    "title": "Test",
    "source_branch": "test",
    "source_project_id": 1,
    "target_branch": "master",
    "target_project_id": 1,
    "state": "opened",
    "merge_status": "can_be_merged",
    "detailed_merge_status": "mergeable",
    "url": "http://192.168.64.1:3005/gitlab-org/gitlab-test/merge_requests/1"
  },
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
    "email": "user_email@gitlab.com"
  },
  "project": {
    "id": 1,
    "name": "Gitlab Test",
    "description": "Atque in sunt eos similique dolores voluptatem.",
    "web_url": "http://192.168.64.1:3005/gitlab-org/gitlab-test",
    "avatar_url": null,
    "git_ssh_url": "git@192.168.64.1:gitlab-org/gitlab-test.git",
    "git_http_url": "http://192.168.64.1:3005/gitlab-org/gitlab-test.git",
    "namespace": "Gitlab Org",
    "visibility_level": 20,
    "path_with_namespace": "gitlab-org/gitlab-test",
    "default_branch": "master",
    "ci_config_path": null
  },
  "commit": {
    "id": "bcbb5ec396a2c0f828686f14fac9b80b780504f2",
    "message": "test\n",
    "title": "test",
    "timestamp": "2016-08-12T17:23:21+02:00",
    "url": "http://example.com/gitlab-org/gitlab-test/commit/bcbb5ec396a2c0f828686f14fac9b80b780504f2",
    "author": {
      "name": "User",
      "email": "user@gitlab.com"
    }
  },
  "builds": [
    {
      "id": 380,
      "stage": "deploy",
      "name": "production",
      "status": "skipped",
      "created_at": "2016-08-12 15:23:28 UTC",
      "started_at": null,
      "finished_at": null,
      "duration": null,
      "queued_duration": null,
      "failure_reason": null,
      "when": "manual",
      "manual": true,
      "allow_failure": false,
      "user": {
        "id": 1,
        "name": "Administrator",
        "username": "root",
        "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
        "email": "admin@example.com"
      },
      "runner": null,
      "artifacts_file": {
        "filename": null,
        "size": null
      },
      "environment": {
        "name": "production",
        "action": "start",
        "deployment_tier": "production"
      }
    },
    {
      "id": 377,
      "stage": "test",
      "name": "test-image",
      "status": "success",
      "created_at": "2016-08-12 15:23:28 UTC",
      "started_at": "2016-08-12 15:26:12 UTC",
      "finished_at": "2016-08-12 15:26:29 UTC",
      "duration": 17.0,
      "queued_duration": 196.0,
      "failure_reason": null,
      "when": "on_success",
      "manual": false,
      "allow_failure": false,
      "user": {
        "id": 1,
        "name": "Administrator",
        "username": "root",
        "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
        "email": "admin@example.com"
      },
      "runner": {
        "id": 380987,
        "description": "shared-runners-manager-6.gitlab.com",
        "runner_type": "instance_type",
        "active": true,
        "is_shared": true,
        "tags": [
          "linux",
          "docker",
          "shared-runner"
        ]
      },
      "artifacts_file": {
        "filename": null,
        "size": null
      },
      "environment": null
    },
    {
      "id": 378,
      "stage": "test",
      "name": "test-build",
      "status": "failed",
      "created_at": "2016-08-12 15:23:28 UTC",
      "started_at": "2016-08-12 15:26:12 UTC",
      "finished_at": "2016-08-12 15:26:29 UTC",
      "duration": 17.0,
      "queued_duration": 196.0,
      "failure_reason": "script_failure",
      "when": "on_success",
      "manual": false,
      "allow_failure": false,
      "user": {
        "id": 1,
        "name": "Administrator",
        "username": "root",
        "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
        "email": "admin@example.com"
      },
      "runner": {
        "id": 380987,
        "description": "shared-runners-manager-6.gitlab.com",
        "runner_type": "instance_type",
        "active": true,
        "is_shared": true,
        "tags": [
          "linux",
          "docker"
        ]
      },
      "artifacts_file": {
        "filename": null,
        "size": null
      },
      "environment": null
    },
    {
      "id": 376,
      "stage": "build",
      "name": "build-image",
      "status": "success",
      "created_at": "2016-08-12 15:23:28 UTC",
      "started_at": "2016-08-12 15:24:56 UTC",
      "finished_at": "2016-08-12 15:25:26 UTC",
      "duration": 17.0,
      "queued_duration": 196.0,
      "failure_reason": null,
      "when": "on_success",
      "manual": false,
      "allow_failure": false,
      "user": {
        "id": 1,
        "name": "Administrator",
        "username": "root",
        "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
        "email": "admin@example.com"
      },
      "runner": {
        "id": 380987,
        "description": "shared-runners-manager-6.gitlab.com",
        "runner_type": "instance_type",
        "active": true,
        "is_shared": true,
        "tags": [
          "linux",
          "docker"
        ]
      },
      "artifacts_file": {
        "filename": null,
        "size": null
      },
      "environment": null
    },
    {
      "id": 379,
      "stage": "deploy",
      "name": "staging",
      "status": "created",
      "created_at": "2016-08-12 15:23:28 UTC",
      "started_at": null,
      "finished_at": null,
      "duration": null,
      "queued_duration": null,
      "failure_reason": null,
      "when": "on_success",
      "manual": false,
      "allow_failure": false,
      "user": {
        "id": 1,
        "name": "Administrator",
        "username": "root",
        "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
        "email": "admin@example.com"
      },
      "runner": null,
      "artifacts_file": {
        "filename": null,
        "size": null
      },
      "environment": {
        "name": "staging",
        "action": "start",
        "deployment_tier": "staging"
      }
    }
  ],
  "source_pipeline": {
    "project": {
      "id": 41,
      "web_url": "https://gitlab.example.com/gitlab-org/upstream-project",
      "path_with_namespace": "gitlab-org/upstream-project"
    },
    "pipeline_id": 30,
    "job_id": 3401
  }
}
```

## Job 이벤트

Job 이벤트는 Job의 상태가 변경될 때 트리거됩니다. 트리거 Job은 제외됩니다.

페이로드의 `commit.id`는 커밋 ID가 아닌 파이프라인 ID입니다.

GitLab 15.1 이상에서 차단된 사용자가 트리거한 Job 이벤트는 처리되지 않습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Job Hook
```

페이로드 예제:

```json
{
  "object_kind": "build",
  "ref": "gitlab-script-trigger",
  "tag": false,
  "before_sha": "2293ada6b400935a1378653304eaf6221e0fdb8f",
  "sha": "2293ada6b400935a1378653304eaf6221e0fdb8f",
  "retries_count": 2,
  "build_id": 1977,
  "build_name": "test",
  "build_stage": "test",
  "build_status": "created",
  "build_created_at": "2021-02-23T02:41:37.886Z",
  "build_started_at": null,
  "build_finished_at": null,
  "build_created_at_iso": "2021-02-23T02:41:37Z",
  "build_started_at_iso": null,
  "build_finished_at_iso": null,
  "build_duration": null,
  "build_queued_duration": 1095.588715,
  "build_allow_failure": false,
  "build_failure_reason": "unknown_failure",
  "pipeline_id": 2366,
  "runner": {
    "id": 380987,
    "description": "shared-runners-manager-6.gitlab.com",
    "runner_type": "project_type",
    "active": true,
    "is_shared": false,
    "tags": [
      "linux",
      "docker"
    ]
  },
  "project_id": 380,
  "project_name": "gitlab-org/gitlab-test",
  "user": {
    "id": 3,
    "name": "User",
    "username": "user",
    "avatar_url": "http://www.gravatar.com/avatar/e32bd13e2add097461cb96824b7a829c?s=80\u0026d=identicon",
    "email": "user@gitlab.com"
  },
  "commit": {
    "id": 2366,
    "name": "Build pipeline",
    "sha": "2293ada6b400935a1378653304eaf6221e0fdb8f",
    "message": "test\n",
    "author_name": "User",
    "author_email": "user@gitlab.com",
    "author_url": "http://192.168.64.1:3005/user",
    "status": "created",
    "duration": null,
    "started_at": null,
    "finished_at": null,
    "started_at_iso": null,
    "finished_at_iso": null
  },
  "repository": {
    "name": "gitlab_test",
    "url": "http://192.168.64.1:3005/gitlab-org/gitlab-test",
    "description": "Atque in sunt eos similique dolores voluptatem.",
    "homepage": "http://192.168.64.1:3005/gitlab-org/gitlab-test",
    "git_ssh_url": "git@192.168.64.1:gitlab-org/gitlab-test.git",
    "git_http_url": "http://192.168.64.1:3005/gitlab-org/gitlab-test.git",
    "visibility_level": 20
  },
  "project": {
    "id": 380,
    "name": "Gitlab Test",
    "description": "Atque in sunt eos similique dolores voluptatem.",
    "web_url": "http://192.168.64.1:3005/gitlab-org/gitlab-test",
    "avatar_url": null,
    "git_ssh_url": "git@192.168.64.1:gitlab-org/gitlab-test.git",
    "git_http_url": "http://192.168.64.1:3005/gitlab-org/gitlab-test.git",
    "namespace": "Gitlab Org",
    "visibility_level": 20,
    "path_with_namespace": "gitlab-org/gitlab-test",
    "default_branch": "master",
    "ci_config_path": null
  },
  "environment": null,
  "source_pipeline": {
    "project": {
      "id": 41,
      "web_url": "https://gitlab.example.com/gitlab-org/upstream-project",
      "path_with_namespace": "gitlab-org/upstream-project"
    },
    "pipeline_id": 30,
    "job_id": 3401
  }
}
```

### 재시도 횟수

`retries_count`는 Job이 재시도인지 여부를 나타내는 정수입니다. `0`은 Job이 재시도되지 않았음을 의미합니다. `1`은 첫 번째 재시도임을 의미합니다.

### 파이프라인 이름

[`workflow:name`](https://docs.gitlab.com/ci/yaml/#workflowname)으로 파이프라인에 사용자 정의 이름을 설정할 수 있습니다. 파이프라인에 이름이 있는 경우 해당 이름이 `commit.name`의 값이 됩니다.

## 배포 이벤트

배포 이벤트는 배포가 다음과 같은 상태일 때 트리거됩니다:

- 시작됨
- 성공
- 실패
- 취소됨

페이로드의 `deployable_id` 및 `deployable_url`은 배포를 실행한 CI/CD Job을 나타냅니다. [API](https://docs.gitlab.com/ci/environments/external_deployment_tools/) 또는 [`trigger` Job](https://docs.gitlab.com/ci/pipelines/downstream_pipelines/)을 통해 배포 이벤트가 발생한 경우 `deployable_url`은 `null`입니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Deployment Hook
```

페이로드 예제:

```json
{
  "object_kind": "deployment",
  "status": "success",
  "status_changed_at":"2021-04-28 21:50:00 +0200",
  "deployment_id": 15,
  "deployable_id": 796,
  "deployable_url": "http://10.126.0.2:3000/root/test-deployment-webhooks/-/jobs/796",
  "environment": "staging",
  "environment_tier": "staging",
  "environment_slug": "staging",
  "environment_external_url": "https://staging.example.com",
  "project": {
    "id": 30,
    "name": "test-deployment-webhooks",
    "description": "",
    "web_url": "http://10.126.0.2:3000/root/test-deployment-webhooks",
    "avatar_url": null,
    "git_ssh_url": "ssh://vlad@10.126.0.2:2222/root/test-deployment-webhooks.git",
    "git_http_url": "http://10.126.0.2:3000/root/test-deployment-webhooks.git",
    "namespace": "Administrator",
    "visibility_level": 0,
    "path_with_namespace": "root/test-deployment-webhooks",
    "default_branch": "master",
    "ci_config_path": "",
    "homepage": "http://10.126.0.2:3000/root/test-deployment-webhooks",
    "url": "ssh://vlad@10.126.0.2:2222/root/test-deployment-webhooks.git",
    "ssh_url": "ssh://vlad@10.126.0.2:2222/root/test-deployment-webhooks.git",
    "http_url": "http://10.126.0.2:3000/root/test-deployment-webhooks.git"
  },
  "short_sha": "279484c0",
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "https://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
    "email": "admin@example.com"
  },
  "user_url": "http://10.126.0.2:3000/root",
  "commit_url": "http://10.126.0.2:3000/root/test-deployment-webhooks/-/commit/279484c09fbe69ededfced8c1bb6e6d24616b468",
  "commit_title": "Add new file"
}
```

## 그룹 멤버 이벤트

- 등급: Premium, Ultimate

이 이벤트는 [그룹 웹훅](https://docs.gitlab.com/user/project/integrations/webhooks/#group-webhooks)에 대해서만 트리거됩니다.

멤버 이벤트는 다음과 같은 경우에 트리거됩니다:

- 사용자가 그룹 멤버로 추가됨
- 사용자의 액세스 수준이 변경됨
- 사용자 액세스의 만료일이 업데이트됨
- 사용자가 그룹에서 제거됨
- 사용자가 그룹에 액세스를 요청함
- 액세스 요청이 거부됨

### 그룹에 멤버 추가

요청 헤더:

```plaintext
X-Gitlab-Event: Member Hook
```

페이로드 예제:

```json
{
  "created_at": "2020-12-11T04:57:22Z",
  "updated_at": "2020-12-11T04:57:22Z",
  "group_name": "webhook-test",
  "group_path": "webhook-test",
  "group_id": 100,
  "user_username": "test_user",
  "user_name": "Test User",
  "user_email": "testuser@webhooktest.com",
  "user_id": 64,
  "group_access": "Guest",
  "group_plan": null,
  "expires_at": "2020-12-14T00:00:00Z",
  "event_name": "user_add_to_group"
}
```

### 멤버 액세스 수준 또는 만료일 업데이트

요청 헤더:

```plaintext
X-Gitlab-Event: Member Hook
```

페이로드 예제:

```json
{
  "created_at": "2020-12-11T04:57:22Z",
  "updated_at": "2020-12-12T08:48:19Z",
  "group_name": "webhook-test",
  "group_path": "webhook-test",
  "group_id": 100,
  "user_username": "test_user",
  "user_name": "Test User",
  "user_email": "testuser@webhooktest.com",
  "user_id": 64,
  "group_access": "Developer",
  "group_plan": null,
  "expires_at": "2020-12-20T00:00:00Z",
  "event_name": "user_update_for_group"
}
```

### 그룹에서 멤버 제거

요청 헤더:

```plaintext
X-Gitlab-Event: Member Hook
```

페이로드 예제:

```json
{
  "created_at": "2020-12-11T04:57:22Z",
  "updated_at": "2020-12-12T08:52:34Z",
  "group_name": "webhook-test",
  "group_path": "webhook-test",
  "group_id": 100,
  "user_username": "test_user",
  "user_name": "Test User",
  "user_email": "testuser@webhooktest.com",
  "user_id": 64,
  "group_access": "Guest",
  "group_plan": null,
  "expires_at": "2020-12-14T00:00:00Z",
  "event_name": "user_remove_from_group"
}
```

### 사용자가 액세스 요청

요청 헤더:

```plaintext
X-Gitlab-Event: Member Hook
```

페이로드 예제:

```json
{
  "created_at": "2020-12-11T04:57:22Z",
  "updated_at": "2020-12-12T08:52:34Z",
  "group_name": "webhook-test",
  "group_path": "webhook-test",
  "group_id": 100,
  "user_username": "test_user",
  "user_name": "Test User",
  "user_email": "testuser@webhooktest.com",
  "user_id": 64,
  "group_access": "Guest",
  "group_plan": null,
  "expires_at": "2020-12-14T00:00:00Z",
  "event_name": "user_access_request_to_group"
}
```

### 액세스 요청이 거부됨

요청 헤더:

```plaintext
X-Gitlab-Event: Member Hook
```

페이로드 예제:

```json
{
  "created_at": "2020-12-11T04:57:22Z",
  "updated_at": "2020-12-12T08:52:34Z",
  "group_name": "webhook-test",
  "group_path": "webhook-test",
  "group_id": 100,
  "user_username": "test_user",
  "user_name": "Test User",
  "user_email": "testuser@webhooktest.com",
  "user_id": 64,
  "group_access": "Guest",
  "group_plan": null,
  "expires_at": "2020-12-14T00:00:00Z",
  "event_name": "user_access_request_denied_for_group"
}
```

## 프로젝트 이벤트

- 등급: Premium, Ultimate

이 이벤트는 [그룹 웹훅](https://docs.gitlab.com/user/project/integrations/webhooks/#group-webhooks)에 대해서만 트리거됩니다.

프로젝트 이벤트는 다음과 같은 경우에 트리거됩니다:

- [그룹에 프로젝트가 생성됨](https://docs.gitlab.com/user/project/integrations/webhook_events/#create-a-project-in-a-group)
- [그룹에서 프로젝트가 삭제됨](https://docs.gitlab.com/user/project/integrations/webhook_events/#delete-a-project-in-a-group)

### 그룹에 프로젝트 생성

요청 헤더:

```plaintext
X-Gitlab-Event: Project Hook
```

페이로드 예제:

```json
{
  "event_name": "project_create",
  "created_at": "2024-10-07T10:43:48Z",
  "updated_at": "2024-10-07T10:43:48Z",
  "name": "project1",
  "path": "project1",
  "path_with_namespace": "group1/project1",
  "project_id": 22,
  "project_namespace_id": 32,
  "owners": [{
    "name": "John",
    "email": "user1@example.com"
  }],
  "project_visibility": "private"
}
```

### 그룹에서 프로젝트 삭제

요청 헤더:

```plaintext
X-Gitlab-Event: Project Hook
```

페이로드 예제:

```json
{
  "event_name": "project_destroy",
  "created_at": "2024-10-07T10:43:48Z",
  "updated_at": "2024-10-07T10:43:48Z",
  "name": "project1",
  "path": "project1",
  "path_with_namespace": "group1/project1",
  "project_id": 22,
  "project_namespace_id": 32,
  "owners": [{
    "name": "John",
    "email": "user1@example.com"
  }],
  "project_visibility": "private"
}
```

## 하위 그룹 이벤트

- 등급: Premium, Ultimate

이 이벤트는 [그룹 웹훅](https://docs.gitlab.com/user/project/integrations/webhooks/#group-webhooks)에 대해서만 트리거됩니다.

하위 그룹 이벤트는 다음과 같은 경우에 트리거됩니다:

- [그룹에 하위 그룹이 생성됨](https://docs.gitlab.com/user/project/integrations/webhook_events/#create-a-subgroup-in-a-group)
- [그룹에서 하위 그룹이 제거됨](https://docs.gitlab.com/user/project/integrations/webhook_events/#remove-a-subgroup-from-a-group)

### 그룹에 하위 그룹 생성

요청 헤더:

```plaintext
X-Gitlab-Event: Subgroup Hook
```

페이로드 예제:

```json
{

  "created_at": "2021-01-20T09:40:12Z",
  "updated_at": "2021-01-20T09:40:12Z",
  "event_name": "subgroup_create",
  "name": "subgroup1",
  "path": "subgroup1",
  "full_path": "group1/subgroup1",
  "group_id": 10,
  "parent_group_id": 7,
  "parent_name": "group1",
  "parent_path": "group1",
  "parent_full_path": "group1"

}
```

### 그룹에서 하위 그룹 제거

이 웹훅은 하위 그룹이 [새 상위 그룹으로 전송](https://docs.gitlab.com/user/group/manage/#transfer-a-group)될 때 트리거되지 않습니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Subgroup Hook
```

페이로드 예제:

```json
{

  "created_at": "2021-01-20T09:40:12Z",
  "updated_at": "2021-01-20T09:40:12Z",
  "event_name": "subgroup_destroy",
  "name": "subgroup1",
  "path": "subgroup1",
  "full_path": "group1/subgroup1",
  "group_id": 10,
  "parent_group_id": 7,
  "parent_name": "group1",
  "parent_path": "group1",
  "parent_full_path": "group1"

}
```

## 기능 플래그 이벤트

기능 플래그 이벤트는 기능 플래그가 켜지거나 꺼질 때 트리거됩니다.

요청 헤더:

```plaintext
X-Gitlab-Event: Feature Flag Hook
```

페이로드 예제:

```json
{
  "object_kind": "feature_flag",
  "project": {
    "id": 1,
    "name":"Gitlab Test",
    "description":"Aut reprehenderit ut est.",
    "web_url":"http://example.com/gitlabhq/gitlab-test",
    "avatar_url":null,
    "git_ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "git_http_url":"http://example.com/gitlabhq/gitlab-test.git",
    "namespace":"GitlabHQ",
    "visibility_level":20,
    "path_with_namespace":"gitlabhq/gitlab-test",
    "default_branch":"master",
    "ci_config_path": null,
    "homepage":"http://example.com/gitlabhq/gitlab-test",
    "url":"http://example.com/gitlabhq/gitlab-test.git",
    "ssh_url":"git@example.com:gitlabhq/gitlab-test.git",
    "http_url":"http://example.com/gitlabhq/gitlab-test.git"
  },
  "user": {
    "id": 1,
    "name": "Administrator",
    "username": "root",
    "avatar_url": "https://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=80&d=identicon",
    "email": "admin@example.com"
  },
  "user_url": "http://example.com/root",
  "object_attributes": {
    "id": 6,
    "name": "test-feature-flag",
    "description": "test-feature-flag-description",
    "active": true
  }
}
```

## 릴리스 이벤트

릴리스 이벤트는 릴리스가 생성, 업데이트 또는 삭제될 때 트리거됩니다.

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `create`
- `update`
- `delete`

요청 헤더:

```plaintext
X-Gitlab-Event: Release Hook
```

페이로드 예제:

```json
{
  "id": 1,
  "created_at": "2020-11-02 12:55:12 UTC",
  "description": "v1.1 has been released",
  "name": "v1.1",
  "released_at": "2020-11-02 12:55:12 UTC",
  "tag": "v1.1",
  "object_kind": "release",
  "project": {
    "id": 2,
    "name": "release-webhook-example",
    "description": "",
    "web_url": "https://example.com/gitlab-org/release-webhook-example",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@example.com/gitlab-org/release-webhook-example.git",
    "git_http_url": "https://example.com/gitlab-org/release-webhook-example.git",
    "namespace": "Gitlab",
    "visibility_level": 0,
    "path_with_namespace": "gitlab-org/release-webhook-example",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "https://example.com/gitlab-org/release-webhook-example",
    "url": "ssh://git@example.com/gitlab-org/release-webhook-example.git",
    "ssh_url": "ssh://git@example.com/gitlab-org/release-webhook-example.git",
    "http_url": "https://example.com/gitlab-org/release-webhook-example.git"
  },
  "url": "https://example.com/gitlab-org/release-webhook-example/-/releases/v1.1",
  "action": "create",
  "assets": {
    "count": 5,
    "links": [
      {
        "id": 1,
        "link_type": "other",
        "name": "Changelog",
        "url": "https://example.net/changelog"
      }
    ],
    "sources": [
      {
        "format": "zip",
        "url": "https://example.com/gitlab-org/release-webhook-example/-/archive/v1.1/release-webhook-example-v1.1.zip"
      },
      {
        "format": "tar.gz",
        "url": "https://example.com/gitlab-org/release-webhook-example/-/archive/v1.1/release-webhook-example-v1.1.tar.gz"
      },
      {
        "format": "tar.bz2",
        "url": "https://example.com/gitlab-org/release-webhook-example/-/archive/v1.1/release-webhook-example-v1.1.tar.bz2"
      },
      {
        "format": "tar",
        "url": "https://example.com/gitlab-org/release-webhook-example/-/archive/v1.1/release-webhook-example-v1.1.tar"
      }
    ]
  },
  "commit": {
    "id": "ee0a3fb31ac16e11b9dbb596ad16d4af654d08f8",
    "message": "Release v1.1",
    "title": "Release v1.1",
    "timestamp": "2020-10-31T14:58:32+11:00",
    "url": "https://example.com/gitlab-org/release-webhook-example/-/commit/ee0a3fb31ac16e11b9dbb596ad16d4af654d08f8",
    "author": {
      "name": "Example User",
      "email": "user@example.com"
    }
  }
}
```

## 마일스톤 이벤트

마일스톤 이벤트는 마일스톤이 생성, 종료, 재개 또는 삭제될 때 트리거됩니다.

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `create`
- `close`
- `reopen`

요청 헤더:

```plaintext
X-Gitlab-Event: Milestone Hook
```

페이로드 예제:

```json
{
  "object_kind": "milestone",
  "event_type": "milestone",
  "project": {
    "id": 1,
    "name": "Gitlab Test",
    "description": "Aut reprehenderit ut est.",
    "web_url": "http://example.com/gitlabhq/gitlab-test",
    "avatar_url": null,
    "git_ssh_url": "git@example.com:gitlabhq/gitlab-test.git",
    "git_http_url": "http://example.com/gitlabhq/gitlab-test.git",
    "namespace": "GitlabHQ",
    "visibility_level": 20,
    "path_with_namespace": "gitlabhq/gitlab-test",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "http://example.com/gitlabhq/gitlab-test",
    "url": "http://example.com/gitlabhq/gitlab-test.git",
    "ssh_url": "git@example.com:gitlabhq/gitlab-test.git",
    "http_url": "http://example.com/gitlabhq/gitlab-test.git"
  },
  "object_attributes": {
    "id": 61,
    "iid": 10,
    "title": "v1.0",
    "description": "First stable release",
    "state": "active",
    "created_at": "2025-06-16 14:10:57 UTC",
    "updated_at": "2025-06-16 14:10:57 UTC",
    "due_date": "2025-06-30",
    "start_date": "2025-06-16",
    "group_id": null,
    "project_id": 1
  },
  "action": "create"
}
```

## 이모지 이벤트

이모지 이벤트는 [이모지 반응](https://docs.gitlab.com/user/emoji_reactions/)이 추가되거나 제거될 때 트리거됩니다. 대상:

- 이슈
- 머지 리퀘스트
- 프로젝트 스니펫
- 위키 페이지
- 다음에 대한 댓글:
  - 이슈
  - 머지 리퀘스트
  - 프로젝트 스니펫
  - 위키 페이지
  - 커밋

페이로드에서 `object_attributes.action`에 사용 가능한 값:

- `award`: 반응 추가
- `revoke`: 반응 제거

요청 헤더:

```plaintext
X-Gitlab-Event: Emoji Hook
```

페이로드 예제:

```json
{
  "object_kind": "emoji",
  "event_type": "award",
  "user": {
    "id": 1,
    "name": "Blake Bergstrom",
    "username": "root",
    "avatar_url": "http://example.com/uploads/-/system/user/avatar/1/avatar.png",
    "email": "[REDACTED]"
  },
  "project_id": 6,
  "project": {
    "id": 6,
    "name": "Flight",
    "description": "Velit fugit aperiam illum deleniti odio sequi.",
    "web_url": "http://example.com/flightjs/Flight",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@example.com/flightjs/Flight.git",
    "git_http_url": "http://example.com/flightjs/Flight.git",
    "namespace": "Flightjs",
    "visibility_level": 20,
    "path_with_namespace": "flightjs/Flight",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "http://example.com/flightjs/Flight",
    "url": "ssh://git@example.com/flightjs/Flight.git",
    "ssh_url": "ssh://git@example.com/flightjs/Flight.git",
    "http_url": "http://example.com/flightjs/Flight.git"
  },
  "object_attributes": {
    "user_id": 1,
    "created_at": "2023-07-04 20:44:11 UTC",
    "id": 1,
    "name": "thumbsup",
    "awardable_type": "Note",
    "awardable_id": 363,
    "updated_at": "2023-07-04 20:44:11 UTC",
    "action": "award",
    "awarded_on_url": "http://example.com/flightjs/Flight/-/issues/42#note_363"
  },
  "note": {
    "attachment": null,
    "author_id": 1,
    "change_position": null,
    "commit_id": null,
    "created_at": "2023-07-04 15:09:55 UTC",
    "discussion_id": "c3d97fd471f210a5dc8b97a409e3bea95ee06c14",
    "id": 363,
    "line_code": null,
    "note": "Testing 123",
    "noteable_id": 635,
    "noteable_type": "Issue",
    "original_position": null,
    "position": null,
    "project_id": 6,
    "resolved_at": null,
    "resolved_by_id": null,
    "resolved_by_push": null,
    "st_diff": null,
    "system": false,
    "type": null,
    "updated_at": "2023-07-04 19:58:46 UTC",
    "updated_by_id": null,
    "description": "Testing 123",
    "url": "http://example.com/flightjs/Flight/-/issues/42#note_363"
  },
  "issue": {
    "author_id": 1,
    "closed_at": null,
    "confidential": false,
    "created_at": "2023-07-04 14:59:43 UTC",
    "description": "Issue description!",
    "discussion_locked": null,
    "due_date": null,
    "id": 635,
    "iid": 42,
    "last_edited_at": null,
    "last_edited_by_id": null,
    "milestone_id": null,
    "moved_to_id": null,
    "duplicated_to_id": null,
    "project_id": 6,
    "relative_position": 18981,
    "state_id": 1,
    "time_estimate": 0,
    "title": "New issue!",
    "updated_at": "2023-07-04 15:09:55 UTC",
    "updated_by_id": null,
    "weight": null,
    "health_status": null,
    "url": "http://example.com/flightjs/Flight/-/issues/42",
    "total_time_spent": 0,
    "time_change": 0,
    "human_total_time_spent": null,
    "human_time_change": null,
    "human_time_estimate": null,
    "assignee_ids": [
      1
    ],
    "assignee_id": 1,
    "labels": [

    ],
    "state": "opened",
    "severity": "unknown"
  }
}
```

## 프로젝트 및 그룹 액세스 토큰 이벤트

액세스 토큰 만료 이벤트는 [액세스 토큰](https://docs.gitlab.com/security/tokens/)이 만료되기 전에 트리거됩니다. 다음 시점에 트리거됩니다:

- 토큰 만료 7일 전
- 토큰 만료 30일 전 (설정 필요)
- 토큰 만료 60일 전 (설정 필요)

30일 및 60일 알림 구성에 대한 자세한 내용은 다음을 참조하세요:

- [프로젝트 액세스 토큰 만료에 대한 추가 웹훅 트리거 추가](https://docs.gitlab.com/user/project/settings/#add-additional-webhook-triggers-for-project-access-token-expiration)
- [그룹 액세스 토큰 만료에 대한 추가 웹훅 트리거 추가](https://docs.gitlab.com/user/group/manage/#add-additional-webhook-triggers-for-group-access-token-expiration)

페이로드에서 `event_name`에 사용 가능한 값:

- `expiring_access_token`

요청 헤더:

```plaintext
X-Gitlab-Event: Resource Access Token Hook
```

프로젝트 페이로드 예제:

```json
{
  "object_kind": "access_token",
  "project": {
    "id": 7,
    "name": "Flight",
    "description": "Eum dolore maxime atque reprehenderit voluptatem.",
    "web_url": "https://example.com/flightjs/Flight",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@example.com/flightjs/Flight.git",
    "git_http_url": "https://example.com/flightjs/Flight.git",
    "namespace": "Flightjs",
    "visibility_level": 0,
    "path_with_namespace": "flightjs/Flight",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "https://example.com/flightjs/Flight",
    "url": "ssh://git@example.com/flightjs/Flight.git",
    "ssh_url": "ssh://git@example.com/flightjs/Flight.git",
    "http_url": "https://example.com/flightjs/Flight.git"
  },
  "object_attributes": {
    "user_id": 90,
    "created_at": "2024-01-24 16:27:40 UTC",
    "id": 25,
    "name": "acd",
    "expires_at": "2024-01-26",
    "last_used_at": "2024-01-20 10:15:30 UTC"
  },
  "event_name": "expiring_access_token"
}
```

그룹 페이로드 예제:

```json
{
  "object_kind": "access_token",
  "group": {
    "group_name": "Twitter",
    "group_path": "twitter",
    "group_id": 35,
    "full_path": "twitter"
  },
  "object_attributes": {
    "user_id": 90,
    "created_at": "2024-01-24 16:27:40 UTC",
    "id": 25,
    "name": "acd",
    "expires_at": "2024-01-26",
    "last_used_at": "2024-01-20 10:15:30 UTC"
  },
  "event_name": "expiring_access_token"
}
```

## 프로젝트 및 그룹 배포 토큰 이벤트

배포 토큰 만료 이벤트는 [배포 토큰](https://docs.gitlab.com/security/tokens/)이 만료되기 전에 트리거됩니다. 다음 시점에 트리거됩니다:

- 토큰 만료 7일 전
- 토큰 만료 30일 전
- 토큰 만료 60일 전

페이로드에서 `event_name`에 사용 가능한 값:

- `expiring_deploy_token`

요청 헤더:

```plaintext
X-Gitlab-Event: Resource Deploy Token Hook
```

프로젝트 페이로드 예제:

```json
{
  "object_kind": "deploy_token",
  "project": {
    "id": 2,
    "name": "Gitlab Test",
    "description": "Voluptates sit architecto quos distinctio.",
    "web_url": "https://gitlab.example.com/gitlab-org/gitlab-test",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@gitlab.example.com:2222/gitlab-org/gitlab-test.git",
    "git_http_url": "https://gitlab.example.com/gitlab-org/gitlab-test.git",
    "namespace": "Gitlab Org",
    "visibility_level": 10,
    "path_with_namespace": "gitlab-org/gitlab-test",
    "default_branch": "master",
    "ci_config_path": null,
    "homepage": "https://gitlab.example.com/gitlab-org/gitlab-test",
    "url": "ssh://git@gitlab.example.com:2222/gitlab-org/gitlab-test.git",
    "ssh_url": "ssh://git@gitlab.example.com:2222/gitlab-org/gitlab-test.git",
    "http_url": "https://gitlab.example.com/gitlab-org/gitlab-test.git"
  },
  "object_attributes": {
    "id": 79,
    "name": "seven-days-6days",
    "expires_at": "2025-08-03 07:57:25 UTC",
    "created_at": "2025-07-28 07:57:25 UTC",
    "revoked": false,
    "deploy_token_type": "project_type"
  },
  "event_name": "expiring_deploy_token"
}
```

## 취약점 이벤트

취약점 이벤트는 다음과 같은 경우에 트리거됩니다:

- 취약점이 생성됨
- 취약점의 [상태가 변경됨](https://docs.gitlab.com/user/application_security/vulnerabilities/#vulnerability-status-values)
- 이슈가 취약점에 연결됨

요청 헤더:

```plaintext
X-Gitlab-Event: Vulnerability Hook
```

페이로드 예제:

```json
{
  "object_kind": "vulnerability",
  "object_attributes": {
    "url": "https://example.com/flightjs/Flight/-/security/vulnerabilities/1",
    "title": "REXML DoS vulnerability",
    "state": "confirmed",
    "project_id": 50,
    "location": {
      "file": "Gemfile.lock",
      "dependency": {
        "package": {
          "name": "rexml"
        },
        "version": "3.3.1"
      }
    },
    "cvss": [
      {
        "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H",
        "vendor": "NVD"
      }
    ],
    "severity": "high",
    "severity_overridden": false,
    "identifiers": [
      {
        "name": "Gemnasium-29dce398-220a-4315-8c84-16cd8b6d9b05",
        "external_id": "29dce398-220a-4315-8c84-16cd8b6d9b05",
        "external_type": "gemnasium",
        "url": "https://gitlab.com/gitlab-org/security-products/gemnasium-db/-/blob/master/gem/rexml/CVE-2024-41123.yml"
      },
      {
        "name": "CVE-2024-41123",
        "external_id": "CVE-2024-41123",
        "external_type": "cve",
        "url": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-41123"
      }
    ],
    "issues": [
      {
        "title": "REXML ReDoS vulnerability",
        "url": "https://example.com/flightjs/Flight/-/issues/1",
        "created_at": "2025-01-08T00:46:14.429Z",
        "updated_at": "2025-01-08T00:46:14.429Z"
      }
    ],
    "report_type": "dependency_scanning",
    "scanner_external_id": "gitlab-sbom-vulnerability-scanner",
    "confidence": "unknown",
    "confidence_overridden": false,
    "confirmed_at": "2025-01-08T00:46:14.413Z",
    "confirmed_by_id": 1,
    "dismissed_at": null,
    "dismissed_by_id": null,
    "resolved_at": null,
    "resolved_by_id": null,
    "auto_resolved": false,
    "resolved_on_default_branch": false,
    "created_at": "2025-01-08T00:46:14.413Z",
    "updated_at": "2025-01-08T00:46:14.413Z"
  }
}
```
