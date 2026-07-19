# GitLab Webhook 수신 사양 (GitLab 전용)

본 문서는 GitLab 프로젝트 webhook을 수신 서버에서 어떻게 처리할지 정의한다. Mattermost·Jira·Notion은 별도 문서로 분리한다. 범위: GitLab이 보내는 요청의 형태, 검증, 이벤트별 본문 구조.

## 핵심 특징 (다른 서비스와의 차이)

GitLab webhook은 다음 특징을 갖는다:

- **헤더로 이벤트 종류 식별**: `X-Gitlab-Event` 헤더 값이 이벤트 종류를 결정한다.
- **이중 식별**: 본문 `object_kind` 필드도 같은 정보를 담는다(예외 있음, 아래).
- **Content-Type 고정**: 항상 `application/json`.
- **검증 토큰**: 헤더 `X-Gitlab-Token`으로 전달. 본문이 아님.
- **모든 이벤트가 같은 엔드포인트로 온다**: 라우트 분리 없이 단일 `POST /webhooks/gitlab`에서 헤더로 분기.

## 요청 공통 사양

### 헤더

GitLab이 webhook 발화 시 보내는 대표 헤더:

| 헤더 | 값 | 용도 |
|---|---|---|
| `Content-Type` | `application/json` | 본문 파싱 |
| `X-Gitlab-Event` | 예: `Push Hook`, `Merge Request Hook`, `Pipeline Hook` | 이벤트 종류 식별 |
| `X-Gitlab-Webhook-UUID` | UUID | webhook 엔드포인트 고유 식별자 |
| `X-Gitlab-Token` | webhook 생성 시 설정한 시크릿 | **서명 검증용** |
| `X-Gitlab-Event-UUID` | UUID | 개별 이벤트 고유 식별자(중복 수신 감지) |

### 응답

수신 서버는 빠르게 응답해야 한다. GitLab은 타임아웃 시 webhook을 실패로 처리·재시도한다.

- 성공: `200 OK` (본문 불필요).
- 검증 실패: `401 Unauthorized`.
- 본문 형식 오류: `400 Bad Request`.
- **긴 처리는 비동기로 미루고 즉시 200을 반환**한다. 수신→저장→`200` 순서.

## 검증 — `X-Gitlab-Token`

1. webhook 생성 시(POST `/projects/{id}/hooks`) `token` 필드에 시크릿 설정.
2. GitLab이 매 요청마다 이 값을 `X-Gitlab-Token` 헤더에 담아 전송.
3. 수신 서버는 환경 변수(`WEBHOOK_GITLAB_TOKEN`)와 헤더 값을 상수 시간 비교(`secrets.compare_digest`).
4. 불일치 시 `401`, 본문 저장 안 함.

참고: `token` 값은 webhook 조회 API 응답에 포함되지 않는다(응답엔 `token_present: true`만). 따라서 시크릿은 수신 서버가 환경 변수로 단독 보관한다.

## 엔드포인트

단일 엔드포인트. 이벤트 분기는 헤더로.

```
POST /webhooks/gitlab
```

## 이벤트 종류와 헤더값·object_kind 매핑

| 이벤트 | `X-Gitlab-Event` | 본문 `object_kind` |
|---|---|---|
| Push | `Push Hook` | `push` |
| Tag push | `Tag Push Hook` | `tag_push` |
| Issue | `Issue Hook` | `issue` |
| Merge request | `Merge Request Hook` | `merge_request` |
| Note(댓글) | `Note Hook` | `note` |
| Pipeline | `Pipeline Hook` | `pipeline` |
| Job(build) | `Build Hook` | `build` |
| Deployment | `Deployment Hook` | `deployment` |
| Release | `Release Hook` | `release` |
| Wiki page | `Wiki Page Hook` | `wiki_page` |
| Milestone | `Milestone Hook` | `milestone` |
| Emoji | `Emoji Hook` | `emoji` |
| Feature flag | `Feature Flag Hook` | `feature_flag` |
| Vulnerability | `Vulnerability Hook` | `vulnerability` |
| Resource access token | `Resource Access Token Hook` | `access_token` |
| Resource deploy token | `Resource Deploy Token Hook` | `deploy_token` |
| Work item | (Issue Hook가 재사용됨) | `issue` 또는 `work_item` |

**초기 검증 우선순위** (test_webhooks.py가 구독하도록 세팅한 이벤트 기준):
Push · Merge Request · Issue · Pipeline · Job · Note. 이 6개가 통합 알림에 가장 유용.

## 이벤트별 본문 구조 (검증에 필요한 최소)

모든 이벤트가 `user`(또는 `user_name`), `project`(또는 `project_id`)를 공통으로 포함한다. 아래는 각 이벤트의 핵심 필드만.

### Push (`Push Hook`)
```json
{
  "object_kind": "push",
  "before": "<sha>", "after": "<sha>",
  "ref": "refs/heads/main",
  "user_name": "...", "user_username": "...", "user_email": "...",
  "project": { "web_url": "...", "path_with_namespace": "..." },
  "commits": [
    { "id": "...", "message": "...", "url": "...",
      "author": { "name": "...", "email": "..." },
      "added": [], "modified": [], "removed": [] }
  ],
  "total_commits_count": 4
}
```
- 한 번 push에 20개 초과 커밋 시 `commits`엔 최신 20개만. 총수는 `total_commits_count`.
- 브랜치 생성만 하고 커밋 없으면 `commits: []`.
- 태그 push는 별도 `Tag Push Hook`(`object_kind: tag_push`).

### Merge Request (`Merge Request Hook`)
```json
{
  "object_kind": "merge_request",
  "event_type": "merge_request",
  "user": { "username": "..." },
  "project": { "web_url": "..." },
  "object_attributes": {
    "action": "open",
    "iid": 16, "title": "...",
    "source_branch": "...", "target_branch": "main",
    "state": "opened",
    "detailed_merge_status": "mergeable",
    "url": ".../-/merge_requests/16",
    "draft": false
  },
  "changes": { },
  "assignees": [], "reviewers": [], "labels": []
}
```
- `object_attributes.action`: `open`/`close`/`reopen`/`update`/`merge`/`approval`/`approved`/`unapproval`/`unapproved`.
- **중요**: `action: update`라도 `changes`가 비어있을 수 있다. 수신 측은 항상 `changes` 내용을 직접 검사해야 한다.
- `oldrev` 필드는 `update` 중 코드 변경이 있을 때만 존재.
- deprecated: `assignee_id`(`assignee_ids` 사용), `work_in_progress`(`draft` 사용).

### Issue (`Issue Hook`)
```json
{
  "object_kind": "issue",
  "event_type": "issue",
  "user": { "username": "..." },
  "project": { "web_url": "..." },
  "object_attributes": {
    "action": "open",
    "iid": 23, "title": "...", "state": "opened",
    "url": ".../-/issues/23",
    "labels": [], "assignee_ids": []
  },
  "changes": { },
  "assignees": [], "labels": []
}
```
- `object_attributes.action`: `open`/`close`/`reopen`/`update`.
- work item(Epic/Task/OKR 등)도 이 훅을 쓴다. 일반 이슈는 `type: "Issue"`, 그 외는 `object_kind: work_item`이거나 `type`이 해당 work item 타입.

### Pipeline (`Pipeline Hook`)
```json
{
  "object_kind": "pipeline",
  "object_attributes": {
    "id": 31, "iid": 3, "ref": "main", "sha": "...",
    "status": "success", "detailed_status": "passed",
    "source": "push", "duration": 63,
    "created_at": "...", "finished_at": "...",
    "url": ".../-/pipelines/31"
  },
  "user": { "username": "..." },
  "project": { "web_url": "..." },
  "commit": { "id": "...", "url": "..." },
  "builds": [ { "name": "...", "status": "...", "stage": "...", "allow_failure": false } ]
}
```
- `status`: `created`/`waiting_for_resource`/`preparing`/`pending`/`running`/`success`/`failed`/`canceled`/`skipped`/`manual`/`scheduled`.
- `builds[]`에 각 job 상태 포함.

### Job / Build (`Build Hook`)
```json
{
  "object_kind": "build",
  "build_id": 1977, "build_name": "test", "build_stage": "test",
  "build_status": "success",
  "build_failure_reason": "unknown_failure",
  "allow_failure": false,
  "pipeline_id": 2366,
  "ref": "...", "sha": "...",
  "project_id": 380, "project_name": "...",
  "user": { "username": "..." }
}
```
- **주의**: 본문 키가 `build_*` 접두사 사용. 다른 이벤트와 구조 다름.
- `commit.id`는 **파이프라인 ID**(커밋 SHA 아님).
- trigger job은 이벤트 발생 안 함.

### Note / 댓글 (`Note Hook`)
```json
{
  "object_kind": "note",
  "event_type": "note",
  "user": { "username": "..." },
  "project": { "web_url": "..." },
  "object_attributes": {
    "note": "댓글 본문",
    "noteable_type": "MergeRequest",
    "action": "create",
    "url": "...#note_1244"
  },
  "merge_request": { },
  "issue": { },
  "commit": { },
  "snippet": { }
}
```
- `object_attributes.noteable_type`: `Commit`/`MergeRequest`/`Issue`/`Snippet`. 어떤 대상에 달린 댓글인지 결정.
- 대상별로 해당 키(`merge_request`/`issue`/`commit`/`snippet`)에 본문 포함.
- `action`: `create`/`update`.
- confidential note는 `event_type: confidential_note`.

## 저장 형식

```text
received/gitlab/
└─ 20260716_143012_a1b2c3.json
```

파일 내용:
```json
{
  "received_at": "2026-07-16T14:30:12+09:00",
  "event": "Push Hook",
  "event_uuid": "<X-Gitlab-Event-UUID>",
  "webhook_uuid": "<X-Gitlab-Webhook-UUID>",
  "client_ip": "203.0.113.10",
  "headers": {
    "content-type": "application/json",
    "x-gitlab-event": "Push Hook"
  },
  "payload": { }
}
```
- `payload`는 원문 그대로 저장. 정규화 금지.
- `X-Gitlab-Token` 값은 헤더에 저장하지 않음(마스킹하거나 제외).
- `X-Gitlab-Event-UUID`로 중복 수신 감지 가능.

## 콘솔 출력

수신 시 한 줄 요약:
```
[2026-07-16 14:30:12] gitlab Push Hook user=kanggihoo ref=refs/heads/main commits=2 → received/gitlab/20260716_143012_a1b2c3.json
```

## 처리 순서

1. `X-Gitlab-Token` 검증 → 실패 시 `401`.
2. 본문 JSON 파싱 → 실패 시 `400`.
3. `X-Gitlab-Event` 헤더로 이벤트 종류 판별.
4. 파일 저장.
5. 콘솔 요약 출력.
6. `200 OK` 반환.

긴 처리(알림 전파, 대시보드 갱신)는 범위 밖. 검증 단계에선 1~6만.

## webhook 생성 시 설정값 (GitLab 측)

test_webhooks.py가 `POST /projects/{id}/hooks`로 생성하는 요청 본문 기준:

```json
{
  "url": "https://hooks.example.com/webhooks/gitlab",
  "enable_ssl_verification": true,
  "token": "<WEBHOOK_GITLAB_TOKEN과 동일>",
  "push_events": true,
  "merge_requests_events": true,
  "issues_events": true,
  "pipeline_events": true,
  "job_events": true,
  "note_events": true
}
```

- 권한: Maintainer(40) 이상 + `api` scope 토큰 필요.
- `enable_ssl_verification`: VPS가 HTTPS면 `true`. self-signed면 임시 `false`(POC 한정).
- 생성 후 `X-Gitlab-Token` 헤더로 검증 토큰이 옴.

## 검증 체크리스트

- [ ] `POST /webhooks/gitlab` 단일 엔드포인트.
- [ ] `X-Gitlab-Token` 상수 시간 비교 (`secrets.compare_digest`).
- [ ] `X-Gitlab-Event` 헤더로 이벤트 분기.
- [ ] 원문 `received/gitlab/*.json` 저장. 토큰 값 제외.
- [ ] `200 OK` 즉시 응답.
- [ ] 콘솔 요약 출력.
- [ ] test_webhooks.py로 실제 발화 후 파일로 형태 확인.

## 원문 참조

- 이벤트 종류·전체 페이로드: https://docs.gitlab.com/user/project/integrations/webhook_events/
- webhook 설정·관리 API: `/api-docs/gitlab_rest_defuddle_markdown/68-hooks/` (28-add, 27-list, 29-retrieve, 30-update, 31-delete)
- webhook 토큰 검증: https://docs.gitlab.com/user/project/integrations/webhooks/

## 다른 서비스는 별도 문서로

Mattermost(form 본문 `token`), Jira(내장 통합 우선 검토), Notion(2025 네이티브 webhook, 권한 미확정)은 각각 별도 사양 문서로 작성한다. GitLab 먼저 검증 완료 후 확장.
