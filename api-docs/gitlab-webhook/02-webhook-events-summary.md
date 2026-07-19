# GitLab 웹훅 이벤트 개발자 가이드 요약

GitLab 웹훅 연동 시 개발자가 알아야 할 핵심 이벤트 종류 및 요청 페이로드 요약 가이드입니다.

---

## 1. 공통 HTTP 요청 헤더 (HTTP Headers)

외부 서버(수신측)에서 요청을 식별하고 검증하기 위해 사용하는 헤더 정보입니다.

* **`X-Gitlab-Event`**: 트리거된 웹훅의 이벤트 유형 이름 (예: `Push Hook`, `Pipeline Hook`).
* **보안 검증용 헤더**:
  * **`webhook-signature` (권장)**: 서명 토큰 설정 시 전송되는 HMAC-SHA256 서명값 (`v1,{signature}`).
  * **`X-Gitlab-Token` (비권장)**: 시크릿 토큰 설정 시 전송되는 평문 토큰 값.

---

## 2. 핵심 웹훅 이벤트 요약

개발 시 가장 빈번하게 활용되는 5가지 핵심 이벤트의 구조 및 필수 필드입니다.

### ① 푸시 이벤트 (Push Hook)
* **트리거**: 리포지토리에 새 커밋을 푸시할 때 발생 (태그 푸시 제외).
* **헤더**: `X-Gitlab-Event: Push Hook`
* **주요 필드 요약**:
  ```json
  {
    "object_kind": "push",
    "event_name": "push",
    "ref": "refs/heads/master",        // 푸시된 브랜치
    "user_name": "John Smith",          // 푸시한 사용자명
    "total_commits_count": 4,           // 전체 푸시된 커밋 수
    "commits": [                        // 최신 커밋 리스트 (최대 20개 제한)
      {
        "id": "b6568db1bc1...",
        "message": "Update translation",
        "timestamp": "2011-12-12T14:27:31+02:00",
        "author": { "name": "Jordi Mallach", "email": "jordi@..." }
      }
    ],
    "repository": {
      "name": "Diaspora",
      "homepage": "http://example.com/mike/diaspora"
    }
  }
  ```

### ② 머지 리퀘스트 이벤트 (Merge Request Hook)
* **트리거**: Merge Request 생성, 수정, 병합(Merge), 종료(Close) 시 발생.
* **헤더**: `X-Gitlab-Event: Merge Request Hook`
* **주요 필드 요약**:
  ```json
  {
    "object_kind": "merge_request",
    "object_attributes": {
      "id": 90,
      "title": "Tempora et eos debitis", // MR 제목
      "state": "opened",                // MR 현재 상태 (opened, closed, merged)
      "action": "open",                 // 이번 트리거 동작 (open, update, close, merge)
      "source_branch": "master",        // 보낼 브랜치
      "target_branch": "markdown",      // 병합 대상 브랜치
      "detailed_merge_status": "checking"
    },
    "user": { "name": "Administrator" }  // 행위자 정보
  }
  ```

### ③ 파이프라인 이벤트 (Pipeline Hook)
* **트리거**: CI/CD 파이프라인의 상태가 변경(성공, 실패, 실행중 등)될 때 발생.
* **헤더**: `X-Gitlab-Event: Pipeline Hook`
* **주요 필드 요약**:
  ```json
  {
    "object_kind": "pipeline",
    "object_attributes": {
      "id": 31,
      "ref": "master",                  // 파이프라인이 실행된 브랜치
      "status": "success",              // 파이프라인 상태 (pending, running, success, failed, canceled)
      "duration": 60,                   // 실행 시간 (초 단위)
      "stages": ["build", "test", "deploy"]
    },
    "project": { "name": "Gitlab Test" }
  }
  ```

### ④ 댓글 이벤트 (Note Hook)
* **트리거**: 커밋, 이슈, MR 등에 새로운 댓글(노트)이 작성되거나 기존 댓글이 수정될 때 발생.
* **헤더**: `X-Gitlab-Event: Note Hook`
* **주요 필드 요약**:
  ```json
  {
    "object_kind": "note",
    "object_attributes": {
      "noteable_type": "MergeRequest",  // 댓글 대상 (Commit, MergeRequest, Issue, Snippet)
      "note": "This MR needs work.",     // 댓글 내용
      "action": "create"                // 동작 (create, update)
    },
    "user": { "name": "Administrator" }
  }
  ```

### ⑤ 이슈 이벤트 (Issue Hook)
* **트리거**: 이슈가 생성, 수정, 종료, 재오픈될 때 발생.
* **헤더**: `X-Gitlab-Event: Issue Hook`
* **주요 필드 요약**:
  ```json
  {
    "object_kind": "issue",
    "object_attributes": {
      "title": "New API: file check",   // 이슈 제목
      "state": "opened",                // 이슈 상태 (opened, closed)
      "action": "open"                  // 동작 (open, close, reopen, update)
    },
    "user": { "name": "Administrator" }
  }
  ```

---

## 3. 웹훅 수신 개발 시 유의사항 (Best Practices)

1. **빠른 응답 (Fast Timeout)**:
   * GitLab은 요청 후 일정 시간(기본 10초 내외) 동안 응답이 없으면 타임아웃 처리함.
   * 무거운 비즈니스 로직(예: 배포 실행, 메일 전송 등)은 요청을 받자마자 **비동기 큐/백그라운드 스레드로 넘기고 200 OK를 즉시 반환**할 것.
2. **멱등성 보장**:
   * 네트워크 유실 등으로 인해 동일 웹훅이 중복 전송될 수 있음. 수신 서버는 중복 처리 방지 로직(예: 커밋 ID 또는 파이프라인 ID 기준 중복 검사)을 설계해야 함.
3. **토큰 검증**:
   * 들어오는 모든 HTTP 요청에 대해 `webhook-signature` 또는 `X-Gitlab-Token` 검증 과정을 거쳐 신뢰할 수 있는 요청만 수락할 것.
