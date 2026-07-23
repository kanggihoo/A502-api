# Merge Requests API 명세서 (관리자 권한 미필요 API)

본 문서는 `_93-merge-requests` 디렉토리 내의 GitLab Merge Requests (머지 리퀘스트 목록 조회, 생성, 수정, 삭제, Diff 변경사항 조회, 리뷰어 지정, MR 병합/리베이스 실행 및 CI 파이프라인 연동) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 37개)

---
---

## 16. List all project merge requests [GET]

### 기본 정보

- **기능:** 특정 프로젝트의 Merge Request 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Request

#### Query parameters
| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `state` | string | N | `opened` | MR 상태 (`opened` \| `closed` \| `locked` \| `merged` \| `all`) | `opened` |
| `search` | string | N | - | 제목/설명 키워드 검색어 | `login` |
| `author_id` | integer | N | - | 작성자 유저 ID | `12` |
| `assignee_id` | integer | N | - | 담당자 유저 ID | `15` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

---

## 19. Retrieve a merge request [GET]

### 기본 정보

- **기능:** 특정 Merge Request 단일 항목의 상세 정보 및 머지 가능 상태를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}`
- **인증:** Bearer Token 필요

---

## 27. Retrieve merge request changes [GET]

### 기본 정보

- **기능:** Merge Request의 전체 변경된 소스코드 패치 Diff 및 추가/삭제 파일 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/changes`
- **인증:** Bearer Token 필요

---


## 09, 10. Global & Group Merge Requests (GET, GET)

- **Endpoints:**
  - `GET /api/v4/merge_requests`: 접근 가능한 전체 프로젝트 통합 MR 목록 조회
  - `GET /api/v4/groups/{id}/merge_requests`: 특정 그룹 범위 내 모든 MR 목록 조회
