# GitLab REST API 명세서

이 문서는 `gitlab-api-test/` 디렉토리 내의 검증용 Python 스크립트들과 실제 응답 결과를 바탕으로 작성된 GitLab REST API(v4) 명세서입니다. 

---

## 공통 설정 및 인증

### API Base URL
- `https://lab.ssafy.com/api/v4` (SSAFY GitLab Self-hosted 기준)

### Request Headers (인증)
사용하는 인증 수단에 따라 요청 헤더에 아래 정보 중 하나를 반드시 포함해야 합니다.

1. **Personal Access Token (PAT) 방식**
   - 헤더 명: `PRIVATE-TOKEN`
   - 예시: `PRIVATE-TOKEN: glpat-xxxxxxxxxxxx`
2. **OAuth2 Access Token 방식**
   - 헤더 명: `Authorization`
   - 예시: `Authorization: Bearer glpat-xxxxxxxxxxxx`

---

## 목차
1. [현재 사용자 정보 조회 (GET /user)](#1-현재-사용자-정보-조회-get-user)
2. [접근 가능 프로젝트 목록 조회 (GET /projects)](#2-접근-가능-프로젝트-목록-조회-get-projects)
3. [프로젝트 상세 조회 (GET /projects/{id})](#3-프로젝트-상세-조회-get-projectsid)
4. [프로젝트 멤버 및 역할 조회 (GET /projects/{id}/members/all)](#4-프로젝트-멤버-및-역할-조회-get-projectsidmembersall)
5. [프로젝트 Merge Request 목록 조회 (GET /projects/{id}/merge_requests)](#5-프로젝트-merge-request-목록-조회-get-projectsidmerge_requests)
6. [프로젝트 Webhook 생성 (POST /projects/{id}/hooks)](#6-프로젝트-webhook-생성-post-projectsidhooks)
7. [프로젝트 Webhook 단건 조회 (GET /projects/{id}/hooks/{hook_id})](#7-프로젝트-webhook-단건-조회-get-projectsidhookshook_id)
8. [프로젝트 Webhook 삭제 (DELETE /projects/{id}/hooks/{hook_id})](#8-프로젝트-webhook-삭제-delete-projectsidhookshook_id)
9. [보호 브랜치 규칙 조회 (GET /projects/{id}/protected_branches)](#9-보호-브랜치-규칙-조회-get-projectsidprotected_branches)
10. [MR 승인 상태 조회 (GET /projects/{id}/merge_requests/{iid}/approvals)](#10-mr-승인-상태-조회-get-projectsidmerge_requestsiidapprovals)
11. [MR 토론 스레드 조회 (GET /projects/{id}/merge_requests/{iid}/discussions)](#11-mr-토론-스레드-조회-get-projectsidmerge_requestsiiddiscussions)
12. [CI 트리거 토큰 목록 조회 (GET /projects/{id}/triggers)](#12-ci-트리거-토큰-목록-조회-get-projectsidtriggers)
13. [CI 환경 변수 목록 조회 (GET /projects/{id}/variables)](#13-ci-환경-변수-목록-조회-get-projectsidvariables)
14. [OAuth2 토큰 갱신 (POST /oauth/token)](#14-oauth2-토큰-갱신-post-oauthtoken)
15. [프로젝트 내 코드 검색 (GET /projects/{id}/search?scope=blobs)](#15-프로젝트-내-코드-검색-get-projectsidsearchscopeblobs)
16. [파일 원문 조회 (GET /projects/{id}/repository/files/{file_path}/raw)](#16-파일-원문-조회-get-projectsidrepositoryfilesfile_pathraw)
17. [프로젝트 push 규칙 조회 (GET /projects/{id}/push_rule)](#17-프로젝트-push-규칙-조회-get-projectsidpush_rule)

---

## 1. 현재 사용자 정보 조회 (GET /user)

### 기본 정보

- **기능:** 현재 인증된 사용자의 프로필 정보 조회
- **Endpoint:** `GET /user`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `read_user` 혹은 `api` scope 권한 필요
- **멱등성:** 지원

### 설명

현재 사용 중인 액세스 토큰의 소유자 계정 정보를 확인하기 위해 호출한다. 계정 활성화 상태(`state`), 유저네임(`username`), 가입 이메일(권한 부여 시) 등의 프로필 메타데이터를 반환하며, 통합 워크스페이스에 진입한 유저의 세션 식별 및 정체 확인에 필수적이다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 (OAuth2 모드 시 필수) | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 (PAT 모드 시 필수) | `glpat-xxxxxxxxxxxx` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 사용자 고유 내부 ID | `30128` |
| `username` | string | 사용자 계정 로그인명 | `11kkh19` |
| `name` | string | 사용자 표시 이름 | `강기호` |
| `state` | string | 계정 상태 (활성 여부) | `active` |
| `web_url` | string | 사용자 프로필 페이지 URL | `https://lab.ssafy.com/11kkh19` |

```json
{
  "id": 30128,
  "username": "11kkh19",
  "name": "강기호",
  "state": "active",
  "web_url": "https://lab.ssafy.com/11kkh19"
}
```

### Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `401` | `Unauthorized` | 토큰 누락 또는 만료 | 토큰 재발급 후 갱신 |

---

## 2. 접근 가능 프로젝트 목록 조회 (GET /projects)

### 기본 정보

- **기능:** 현재 사용자가 접근 가능한 프로젝트 목록 조회
- **Endpoint:** `GET /projects`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

현재 로그인한 사용자가 구성원(`membership=true`)으로 포함되어 있어 접근 권한을 가지는 프로젝트 목록을 수집한다. 통합 워크스페이스에서 관리 대상을 자동 감지하거나, 사용자가 선택할 수 있는 프로젝트 리스트를 구성하기 위해 사용한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 | `glpat-xxxxxxxxxxxx` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `membership` | boolean | N | `false` | 멤버십이 있는 프로젝트만 필터링 | `true` |
| `per_page` | integer | N | `20` | 페이지당 반환 개수 (최대 `100`) | `20` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 프로젝트 고유 ID | `1383726` |
| `path` | string | 프로젝트 경로명 | `ssafy-test` |
| `path_with_namespace` | string | 네임스페이스 포함 경로 | `11kkh19/ssafy-test` |
| `web_url` | string | 프로젝트 웹 페이지 URL | `https://lab.ssafy.com/11kkh19/ssafy-test` |

```json
[
  {
    "id": 1383726,
    "path": "ssafy-test",
    "path_with_namespace": "11kkh19/ssafy-test",
    "web_url": "https://lab.ssafy.com/11kkh19/ssafy-test"
  }
]
```

### Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `401` | `Unauthorized` | 유효하지 않은 자격 증명 | 인증 정보 점검 |

---

## 3. 프로젝트 상세 조회 (GET /projects/{id})

### 기본 정보

- **기능:** 특정 프로젝트의 상세 정보 단건 조회
- **Endpoint:** `GET /projects/{id}`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

프로젝트의 고유 ID 또는 URL-encoded 경로(`path_with_namespace`)를 입력받아 기본 브랜치(`default_branch`), 보관 여부(`archived`), 웹 주소 등을 세부적으로 조회한다. 연동하려는 특정 프로젝트의 존재 유무 및 설정을 실시간 검증할 목적으로 사용한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 | `glpat-xxxxxxxxxxxx` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID 또는 URL-encoded 경로 | `11kkh19%2Fssafy-test` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 프로젝트 고유 ID | `1383726` |
| `path_with_namespace` | string | 네임스페이스가 결합된 고유 경로 | `11kkh19/ssafy-test` |
| `default_branch` | string | 기본 브랜치 이름 | `master` |
| `web_url` | string | 웹 UI 접근 URL | `https://lab.ssafy.com/11kkh19/ssafy-test` |
| `archived` | boolean | 프로젝트 보관 처리 여부 | `false` |

```json
{
  "id": 1383726,
  "path_with_namespace": "11kkh19/ssafy-test",
  "default_branch": "master",
  "web_url": "https://lab.ssafy.com/11kkh19/ssafy-test",
  "archived": false
}
```

### Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `404` | `Not Found` | 존재하지 않는 프로젝트이거나 접근 권한 없음 | 프로젝트 ID 또는 경로 인코딩 방식 확인 |

---

## 4. 프로젝트 멤버 및 역할 조회 (GET /projects/{id}/members/all)

### 기본 정보

- **기능:** 상속된 그룹 멤버를 포함한 프로젝트의 전체 구성원 및 역할 조회
- **Endpoint:** `GET /projects/{id}/members/all`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

프로젝트에 명시적으로 추가된 구성원뿐만 아니라 상위 그룹으로부터 권한을 상속받은 모든 멤버의 계정 정보와 접근 역할(`access_level`)을 가져온다. 팀원들이 가지고 있는 권한(예: Maintainer, Developer 등)에 맞춰 통합 워크스페이스의 기능 노출 및 가용 한도를 제어할 때 참고한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 | `glpat-xxxxxxxxxxxx` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID 또는 URL-encoded 경로 | `11kkh19%2Fssafy-test` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `per_page` | integer | N | `20` | 페이지당 반환 개수 | `50` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `username` | string | 유저네임 | `11kkh19` |
| `name` | string | 표시 이름 | `강기호` |
| `access_level` | integer | 역할 권한 수치 (50: Owner, 40: Maintainer, 30: Developer) | `50` |
| `state` | string | 사용자 계정 상태 | `active` |

```json
[
  {
    "username": "11kkh19",
    "name": "강기호",
    "access_level": 50,
    "state": "active"
  }
]
```

### 주의 사항
- 권한 수치(`access_level`) 매핑 정보는 다음과 같습니다:
  - `30` : Developer
  - `40` : Maintainer (팀장 역할 전제)
  - `50` : Owner
- 상속된 권한을 포함하지 않는 단독 멤버만 볼 때는 `/members/all` 대신 `/members` 엔드포인트를 사용합니다.

---

## 5. 프로젝트 Merge Request 목록 조회 (GET /projects/{id}/merge_requests)

### 기본 정보

- **기능:** 프로젝트 내에 존재하는 Merge Request(MR) 목록 조회
- **Endpoint:** `GET /projects/{id}/merge_requests`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

지정된 프로젝트 내에서 열려 있는(`state=opened`) 리뷰 대상 Merge Request 목록을 가져온다. 작성 중인 임시 상태(`draft`) 여부 및 자동 머지 가능 상태(`detailed_merge_status`)를 구분해 팀원들이 행동해야 할 코드 리뷰 대기 목록을 구성하는 데 사용한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 | `glpat-xxxxxxxxxxxx` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID 또는 URL-encoded 경로 | `11kkh19%2Fssafy-test` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `state` | string | N | `opened` | MR의 상태 (`opened`, `closed`, `locked`, `merged`, `all`) | `opened` |
| `per_page` | integer | N | `20` | 페이지당 반환 개수 | `20` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | MR 고유 시스템 ID | `12345` |
| `iid` | integer | 프로젝트 내부에서의 MR 일련번호 | `1` |
| `title` | string | MR 제목 | `feat: [S15P11A502-23] OAuth 로그인 구현` |
| `state` | string | 현재 상태 | `opened` |
| `draft` | boolean | 임시 작성(Work In Progress) 상태 여부 | `false` |
| `detailed_merge_status` | string | 상세 병합 가능 상태 | `mergeable` |
| `web_url` | string | MR의 GitLab 웹 경로 | `https://lab.ssafy.com/s15-webmobile1-sub1/S15P11A502/-/merge_requests/1` |

```json
[
  {
    "id": 12345,
    "iid": 1,
    "title": "feat: [S15P11A502-23] OAuth 로그인 구현",
    "state": "opened",
    "draft": false,
    "detailed_merge_status": "mergeable",
    "web_url": "https://lab.ssafy.com/s15-webmobile1-sub1/S15P11A502/-/merge_requests/1"
  }
]
```

---

## 6. 프로젝트 Webhook 생성 (POST /projects/{id}/hooks)

### 기본 정보

- **기능:** 프로젝트 이벤트 발생 시 호출할 시스템 Webhook 등록
- **Endpoint:** `POST /projects/{id}/hooks`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 프로젝트의 **Maintainer(40)** 이상 역할 필수
- **멱등성:** 미지원 (동일 URL에 대해 중복 생성이 가능하므로 사전 존재 여부 조회가 권장됨)

### 설명

통합 대시보드나 알림 봇에서 실시간 이벤트를 수신하도록 프로젝트 단위의 Webhook을 구성한다. Push, Merge Request, Issue, Pipeline, Job, Note(댓글) 등의 이벤트가 일어날 때 수신 시스템의 URL로 데이터(Payload)가 실시간 POST로 발송되도록 지시한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | OAuth2 액세스 토큰 | `Bearer {accessToken}` |
| `PRIVATE-TOKEN` | N | 개인 액세스 토큰 | `glpat-xxxxxxxxxxxx` |
| `Content-Type` | Y | 요청 페이로드 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID 또는 URL-encoded 경로 | `1373907` |

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `url` | string | Y | - | 실시간 이벤트를 송신할 대상 서버 Endpoint | `https://ssafy.kkh-hub.tech/webhooks/gitlab` |
| `enable_ssl_verification`| boolean | N | `true` | SSL 인증서 검증 여부 (사설망의 경우 `false` 권장) | `false` |
| `token` | string | N | - | 요청 헤더(`X-Gitlab-Token`)로 전송되어 페이로드가 유효한지 검증하는 시크릿 키 | `gitlab-api-test-poc` |
| `push_events` | boolean | N | `true` | push 이벤트 트리거 여부 | `true` |
| `merge_requests_events` | boolean | N | `false` | Merge Request 생성/변경/병합 트리거 여부 | `true` |
| `issues_events` | boolean | N | `false` | 이슈 생성/변경 트리거 여부 | `true` |
| `pipeline_events` | boolean | N | `false` | CI 파이프라인 시작/종료 트리거 여부 | `true` |
| `job_events` | boolean | N | `false` | CI 잡(job)의 상태 변화 트리거 여부 | `true` |
| `note_events` | boolean | N | `false` | 댓글 및 리뷰 스레드 작성 트리거 여부 | `true` |

```json
{
  "url": "https://ssafy.kkh-hub.tech/webhooks/gitlab",
  "enable_ssl_verification": false,
  "token": "gitlab-api-test-poc",
  "push_events": true,
  "merge_requests_events": true,
  "issues_events": true,
  "pipeline_events": true,
  "job_events": true,
  "note_events": true
}
```

### Response

#### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 Webhook 고유 ID | `810891` |
| `url` | string | 대상 수신 URL | `https://ssafy.kkh-hub.tech/webhooks/gitlab` |
| `push_events` | boolean | Push 이벤트 활성화 여부 | `true` |
| `merge_requests_events` | boolean | MR 이벤트 활성화 여부 | `true` |
| `issues_events` | boolean | 이슈 이벤트 활성화 여부 | `true` |
| `pipeline_events` | boolean | 파이프라인 이벤트 활성화 여부 | `true` |
| `job_events` | boolean | 잡 이벤트 활성화 여부 | `true` |
| `note_events` | boolean | 댓글 및 스레드 이벤트 활성화 여부 | `true` |
| `enable_ssl_verification`| boolean | SSL 인증 검증 여부 | `false` |
| `created_at` | string | 생성 시각 | `2026-07-21T12:35:34.589+09:00` |

```json
{
  "id": 810891,
  "url": "https://ssafy.kkh-hub.tech/webhooks/gitlab",
  "push_events": true,
  "merge_requests_events": true,
  "issues_events": true,
  "pipeline_events": true,
  "job_events": true,
  "note_events": true,
  "enable_ssl_verification": false,
  "created_at": "2026-07-21T12:35:34.589+09:00"
}
```

### Errors

| HTTP 상태 | 코드 | 발생 조건 | 처리 방법 |
|---:|---|---|---|
| `403` | `Forbidden` | 관리자 또는 Maintainer 권한이 없는 계정으로 접근 시도 | 계정 역할 상향 조정 요청 또는 적절한 토큰 활용 |

---

## 7. 프로젝트 Webhook 단건 조회 (GET /projects/{id}/hooks/{hook_id})

### 기본 정보

- **기능:** 등록된 특정 Webhook의 상세 정보 확인
- **Endpoint:** `GET /projects/{id}/hooks/{hook_id}`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 **Maintainer(40)** 권한 필요
- **멱등성:** 지원

### 설명

프로젝트에 이미 설치된 Webhook 중 하나를 골라, 어떤 이벤트들을 구독 중인지와 보안 설정 옵션이 제대로 활성화되어 있는지(예: SSL 검증, 트리거 설정) 단건 조회한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID 또는 URL-encoded 경로 | `1373907` |
| `hook_id` | integer | Y | 대상 Webhook ID | `810891` |

### Response

#### `200 OK`

```json
{
  "id": 810891,
  "url": "https://ssafy.kkh-hub.tech/webhooks/gitlab",
  "push_events": true,
  "merge_requests_events": true,
  "pipeline_events": false,
  "enable_ssl_verification": false
}
```

---

## 8. 프로젝트 Webhook 삭제 (DELETE /projects/{id}/hooks/{hook_id})

### 기본 정보

- **기능:** 구성해 놓은 특정 Webhook 영구 정지 및 해제
- **Endpoint:** `DELETE /projects/{id}/hooks/{hook_id}`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 **Maintainer(40)** 권한 필요
- **멱등성:** 지원

### 설명

더 이상 알림 수신을 할 필요가 없거나, 이전 연결 주소가 유효하지 않을 때 등록된 Webhook을 안전하게 지운다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1373907` |
| `hook_id` | integer | Y | 삭제할 Webhook ID | `810891` |

### Response

#### `204 No Content`
성공 시 별도의 JSON 본문 없이 HTTP 상태 코드 `204`만 반환된다.

---

## 9. 보호 브랜치 규칙 조회 (GET /projects/{id}/protected_branches)

### 기본 정보

- **기능:** 프로젝트의 보호 브랜치 설정 목록 조회
- **Endpoint:** `GET /projects/{id}/protected_branches`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

프로젝트 내에 보호 브랜치로 정의되어 있는 규칙(예: `main`, `master`)들과, 해당 브랜치에 직접 Push하거나 Merge할 수 있도록 승인된 접근 최소 권한 역할을 조회한다. 소스 코드 형상 관리 원칙이 잘 지켜지고 있는지 모니터링하기 위해 사용한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1373907` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `name` | string | 보호 대상 브랜치 이름/패턴 | `main` |
| `push_access_levels` | array | Push 가능 권한 조건 및 라벨 | `[{ "access_level": 40, "access_level_description": "Maintainers" }]` |
| `merge_access_levels`| array | Merge 가능 권한 조건 및 라벨 | `[{ "access_level": 40, "access_level_description": "Maintainers" }]` |

```json
[
  {
    "name": "main",
    "push_access_levels": [
      {
        "access_level": 40,
        "access_level_description": "Maintainers"
      }
    ],
    "merge_access_levels": [
      {
        "access_level": 40,
        "access_level_description": "Maintainers"
      }
    ]
  }
]
```

---

## 10. MR 승인 상태 조회 (GET /projects/{id}/merge_requests/{iid}/approvals)

### 기본 정보

- **기능:** 개별 Merge Request의 요약형 승인 상태 확인
- **Endpoint:** `GET /projects/{id}/merge_requests/{iid}/approvals`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

Merge Request의 승인 여부(`approved`), 로그인한 계정이 이미 승인을 눌렀는지 여부(`user_has_approved`), 그리고 추가 승인이 필요한 기준 등을 요약하여 제공받는다. 병합 승인 제어가 작동 중일 때 머지 전 최종 관문을 검사하기 위해 쓴다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1373907` |
| `iid` | integer | Y | Merge Request 고유 IID | `1` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `approved` | boolean | MR 최종 승인 조건 충족 여부 | `true` |
| `user_has_approved` | boolean | 호출한 유저가 승인했는지 여부 | `false` |
| `user_can_approve` | boolean | 호출한 유저가 승인 권한이 있는지 여부 | `true` |
| `approved_by` | array | 승인한 유저들의 정보 목록 | `[{ "user": { "username": "11kkh19", "name": "강기호" } }]` |

```json
{
  "approved": true,
  "user_has_approved": false,
  "user_can_approve": true,
  "approved_by": [
    {
      "user": {
        "username": "11kkh19",
        "name": "강기호"
      }
    }
  ]
}
```

### 주의 사항
- 이 API는 approvals의 **요약 정보**만 반환합니다. 규칙별 상세 승인 상태 조회가 필요하면 `/merge_requests/{iid}/approval_state` 엔드포인트를 호출하십시오.

---

## 11. MR 토론 스레드 조회 (GET /projects/{id}/merge_requests/{iid}/discussions)

### 기본 정보

- **기능:** MR 내의 코드 리뷰 스레드 및 토론 내역 조회
- **Endpoint:** `GET /projects/{id}/merge_requests/{iid}/discussions`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

Merge Request 내에서 진행되고 있는 모든 코드 리뷰 토론 스레드를 수집한다. 특정 논의가 해결 처리(`resolved`)되었는지 식별하고, 시스템 알림 외에 실제 개발자 간 오간 피드백 데이터를 워크스페이스에 통합하여 보여주기 위해 조회한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1373907` |
| `iid` | integer | Y | Merge Request 고유 IID | `1` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 스레드 고유 ID | `abc123xyz` |
| `individual_note` | boolean | 스레드가 아닌 단발성 메모 여부 | `false` |
| `notes` | array | 스레드에 작성된 노트 목록 | `[ ... ]` |
| `notes.resolvable` | boolean | 해결 처리가 필요한 성격의 리뷰 노트인지 여부 | `true` |
| `notes.resolved` | boolean | 해결 완료 처리되었는지 여부 | `true` |

```json
[
  {
    "id": "abc123xyz",
    "individual_note": false,
    "notes": [
      {
        "id": 999,
        "body": "코드 리뷰 코멘트입니다.",
        "author": {
          "username": "11kkh19",
          "name": "강기호"
        },
        "system": false,
        "created_at": "2026-07-21T13:51:49.000+09:00",
        "resolvable": true,
        "resolved": true
      }
    ]
  }
]
```

---

## 12. CI 트리거 토큰 목록 조회 (GET /projects/{id}/triggers)

### 기본 정보

- **기능:** 파이프라인 외부 트리거 토큰 목록 조회
- **Endpoint:** `GET /projects/{id}/triggers`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 **Maintainer(40)** 권한 필요
- **멱등성:** 지원

### 설명

외부 Jenkins 빌드 연동이나 스케줄러 등 API 호출을 통해 CI를 돌리는 트리거 토큰 목록을 조회한다. 보안 설계 준수를 위해 조회 결과의 토큰 원문 정보(`token`)는 반드시 마스킹 처리하여 안전하게 보관 및 출력해야 한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1383726` |

### Response

#### `200 OK`

```json
[
  {
    "id": 12,
    "description": "Jenkins trigger",
    "token": "glptt-***",
    "last_used": "2026-07-21T12:00:00Z",
    "expires_at": null,
    "owner": {
      "username": "11kkh19"
    }
  }
]
```

### 주의 사항
- **보안 가이드라인:** 트리거 토큰(`token`) 필드는 평문 비밀 키 정보이므로, 터미널 로그 출력이나 리포트 저장 시 반드시 `***`로 치환하는 마스킹 로직을 구현해야 합니다.

---

## 13. CI/CD 환경 변수 목록 조회 (GET /projects/{id}/variables)

### 기본 정보

- **기능:** 프로젝트 빌드 환경 변수 및 보안 키 목록 조회
- **Endpoint:** `GET /projects/{id}/variables`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 **Maintainer(40)** 권한 필요
- **멱등성:** 지원

### 설명

CI/CD 파이프라인이 실행될 때 컨테이너 내부에 주입되는 프로젝트 환경 변수 설정을 수집한다. 해당 변수가 마스킹 처리(`masked`)되었거나 노출 제어(`protected`)가 걸려 있는지 등의 메타정보만 진단용으로 활용하며, 보안 강화를 위해 실제 주입된 값(`value`)은 데이터 반환 스키마에 수집되지 않도록 엄격히 관리해야 한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1383726` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `key` | string | 환경 변수 이름 | `DATABASE_URL` |
| `variable_type` | string | 변수 구분 (`env_var` 또는 `file`) | `env_var` |
| `protected` | boolean | 보호 브랜치/태그 빌드 시에만 전송 여부 | `true` |
| `masked` | boolean | 러너 로그에서 자동 마스킹 필터링 여부 | `true` |
| `environment_scope` | string | 변수가 적용되는 환경 범위 | `*` |

```json
[
  {
    "key": "DATABASE_URL",
    "variable_type": "env_var",
    "protected": true,
    "masked": true,
    "hidden": false,
    "raw": false,
    "environment_scope": "*"
  }
]
```

### 주의 사항
- **보안 제약:** 이 API의 실제 응답 바디에는 평문 값인 `"value": "password"` 필드가 담겨서 날아옵니다. 통계나 진단 정보를 수집하여 외부에 노출해야 한다면, 반드시 `value` 필드를 버리거나 마스킹하여 관리 저장소에 저장해야 합니다.

---

## 14. OAuth2 토큰 갱신 (POST /oauth/token)

### 기본 정보

- **기능:** refresh_token을 활용한 새로운 access_token 발행
- **Endpoint:** `POST /oauth/token`
- **인증:** 불필요 (OAuth Application 자격 정보 전송 필요)
- **권한:** 없음
- **멱등성:** 미지원 (갱신을 요청하면 이전의 refresh_token도 무효화되는 경우가 대다수임)

### 설명

만료된 OAuth2 액세스 토큰을 갱신하기 위해 인증 서버에 토큰 발급을 재요청한다. GitLab은 한 번 사용한 리프레시 토큰을 폐기하고 새로운 세트의 토큰을 내어주는 `rotate-on-use` 정책을 채택하고 있으므로, 갱신된 새로운 `refresh_token`과 `access_token` 쌍을 즉시 구성 정보(.env 파일 등)에 덮어써서 동기화해 주어야 한다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Content-Type` | Y | 요청 폼 인코딩 형식 | `application/x-www-form-urlencoded` |

#### Body (x-www-form-urlencoded)

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `client_id` | string | Y | - | GitLab Application 클라이언트 ID | `app_client_id_123` |
| `client_secret` | string | N | - | GitLab Application 시크릿 키 | `app_secret_abc` |
| `refresh_token` | string | Y | - | 기존에 소지하고 있던 리프레시 토큰 | `glrt-xxxxxxxxxxxx` |
| `grant_type` | string | Y | `refresh_token` | 인증 방식 | `refresh_token` |
| `redirect_uri` | string | N | - | 인증 시 등록한 콜백 URI | `https://ssafy.kkh-hub.tech/oauth/callback` |

```bash
client_id=app_client_id_123&refresh_token=glrt-xxxxxxxxxxxx&grant_type=refresh_token
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `access_token` | string | 새로 발행된 API Access Token | `glpat-newaccess123` |
| `token_type` | string | 토큰 종류 | `Bearer` |
| `expires_in` | integer | 토큰 유효 기간 (초 단위) | `7200` |
| `refresh_token` | string | 다음 갱신 시 사용할 리프레시 토큰 (rotate-on-use) | `glrt-newrefresh456` |
| `scope` | string | 권한 범위 목록 | `api read_user` |
| `created_at` | integer | 생성 타임스탬프 (에포크 시간) | `1784567890` |

```json
{
  "access_token": "glpat-newaccess123",
  "token_type": "Bearer",
  "expires_in": 7200,
  "refresh_token": "glrt-newrefresh456",
  "scope": "api read_user",
  "created_at": 1784567890
}
```

### 주의 사항
- **중요(Rotate-on-use):** 갱신에 성공하자마자 이전 토큰들은 모두 파기됩니다. 새로 반환된 `refresh_token`을 즉각 영속 저장하지 않을 경우, 차기 만료 시 복구가 불가능하여 사용자가 로그아웃을 하고 OAuth 인증 동의 절차를 처음부터 다시 수행해야 할 위험이 있습니다.

---

## 15. 프로젝트 내 코드 검색 (GET /projects/{id}/search?scope=blobs)

### 기본 정보

- **기능:** 프로젝트 내의 파일 본문(코드) 내용 검색
- **Endpoint:** `GET /projects/{id}/search`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_api` scope 권한 필요
- **멱등성:** 지원

### 설명

프로젝트 내에 존재하는 소스 코드 텍스트(blobs) 중에서 찾고자 하는 텍스트(예: `README`, `TODO`)를 검색하여 매칭된 파일 목록, 상대 경로, 시작 라인번호 등을 돌려받는다. 

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `scope` | string | Y | - | 검색할 범위 필터 (`blobs`, `issues`, `merge_requests`, `notes` 등) | `blobs` |
| `search` | string | Y | - | 검색할 키워드 | `README` |

### Response

#### `200 OK`

```json
[
  {
    "basename": "README",
    "path": "README.md",
    "filename": "README.md",
    "ref": "master",
    "startline": 1,
    "project_id": 1383726
  }
]
```

### 주의 사항
- 코드 검색 범위인 `scope=blobs` 대신에 어드민 용도의 API를 오용하면 권한 에러(403)가 납니다. 범용 검색 엔드포인트를 사용해야 합니다.

---

## 16. 파일 원문 조회 (GET /projects/{id}/repository/files/{file_path}/raw)

### 기본 정보

- **기능:** 저장소 내 특정 파일의 원문(raw) 텍스트 가져오기
- **Endpoint:** `GET /projects/{id}/repository/files/{file_path}/raw`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` 또는 `read_repository` scope 권한 필요
- **멱등성:** 지원

### 설명

특정 디렉토리 경로에 적힌 소스 파일의 가공되지 않은 텍스트 내용(예: Markdown 원문, 설정 파일 본문)을 가져온다. 대시보드 내에서 설정 파일이나 README.md 파일의 상단을 미리보기 형태로 표시하는 유스케이스에 사용한다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1383726` |
| `file_path` | string | Y | URL-encoded 처리된 파일 경로 | `docs%2FREADME.md` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ref` | string | N | default 브랜치 | 조회 타깃 브랜치나 커밋 해시 키 | `develop` |

### Response

#### `200 OK`
응답 데이터는 JSON이 아니며, 파일의 실제 원문 데이터가 `text/plain` 혹은 바이너리 바이트 스트림으로 반환됩니다.

```markdown
# A502 API 분석·POC 워크스페이스
이 저장소는 실제 SSAFY 프로젝트를 시작하기 전에...
```

### 주의 사항
- 파일 경로 중 `/` 문자는 반드시 퍼센트 인코딩(`%2F`)을 완료해 주어야 라우팅 오류(404)를 막을 수 있습니다.
- 대용량 파일 조회 시에는 성능과 대역폭을 고려해 미리 헤더 등으로 파일 크기를 체크하는 조치가 수반되어야 합니다.

---

## 17. 프로젝트 push 규칙 조회 (GET /projects/{id}/push_rule)

### 기본 정보

- **기능:** 프로젝트 단위에 적용된 Push 제약 조건 진단
- **Endpoint:** `GET /projects/{id}/push_rule`
- **인증:** Bearer Token 또는 PRIVATE-TOKEN 필요
- **권한:** `api` scope 및 **Premium/Ultimate 라이선스 권한** 필요
- **멱등성:** 지원

### 설명

팀원들이 커밋 메시지 규칙을 위반하거나, 원하지 않는 비밀번호/토큰 정보 등을 강제로 Push하여 올리지 못하도록 제한하는 `push_rule` 보안 환경 설정 상태를 가져온다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string / integer | Y | 프로젝트 고유 ID | `1373907` |

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `commit_message_regex` | string | 커밋 시 요구할 메시지 규격 정규식 | `(feat\|fix\|docs\|chore\|test): \[S15P11A502-\d+\].+` |
| `prevent_secrets` | boolean | 비밀 키/토큰 노출 자동 차단 규칙 활성 여부 | `true` |
| `deny_delete_tag` | boolean | 태그 삭제 불허 처리 여부 | `true` |
| `reject_unsigned_commits`| boolean| GPG 서명 없는 커밋 거부 여부 | `false` |

```json
{
  "id": 456,
  "project_id": 1373907,
  "commit_message_regex": "(feat|fix|docs|chore|test): \\[S15P11A502-\\d+\\].+",
  "branch_name_regex": null,
  "deny_delete_tag": true,
  "member_check": false,
  "prevent_secrets": true,
  "max_file_size": 10,
  "reject_unsigned_commits": false
}
```

### 주의 사항
- **중요 (오타 주의):** API의 경로명이 복수형(`push_rules`)이 아닌 단수형(`push_rule`)입니다. 
- **에디션 및 권한 제약:** GitLab의 무료 에디션(Free Edition)에서는 이 기능을 활성화할 수 없거나 요청 시 `403 Forbidden` 또는 `404 Not Found`가 반환됩니다. 해당 에러 응답 수신 시, 이를 에러 장애 상황이 아닌 라이선스 제약(에디션 부족)으로 정상 판정하고 기록을 정리하는 방어적 처리가 필요합니다.

---

## 공통 에러 응답 규격

GitLab REST API v4는 오류 발생 시 아래 표와 같은 HTTP 상태 코드를 활용하며, Response Body에 JSON 객체 형태로 상세 에러 정보를 포함합니다.

| HTTP 상태 | 발생 조건 | 설명 및 해결 방안 |
|---:|---|---|
| `400` | Bad Request | 잘못된 파라미터(필수 필드 누락, 지원하지 않는 scope 값 전달 등). 응답 바디를 참고해 요청 교정 |
| `401` | Unauthorized | 토큰 누락, 잘못된 토큰, 혹은 토큰 만료. OAuth2 토큰 갱신 API(`POST /oauth/token`)를 통해 갱신 후 재수행 |
| `403` | Forbidden | 요청 자격(토큰의 scope, 사용자 권한 레벨)이 해당 기능을 처리하기에 부족함. 혹은 GitLab 에디션의 제약 발생 |
| `404` | Not Found | 프로젝트 ID가 잘못되었거나, 파일이 없거나, 혹은 권한이 아예 없어 프로젝트 존재 자체가 마스킹됨 |
| `429` | Rate Limited | 단위 시간당 호출 횟수 임계치 도달. 응답 헤더의 `RateLimit`을 확인하고 대기 후 시도 |
| `500` | Internal Server Error | GitLab 서버 내부 장애. 잠시 후 재시도 |

#### 에러 응답 바디 예시
```json
{
  "message": "403 Forbidden - push_rule은 Premium 이상의 에디션 라이선스가 요구됩니다."
}
```
또는
```json
{
  "error": "invalid_grant",
  "error_description": "The provided authorization grant is invalid, expired, or revoked."
}
```
