# Merge Requests API 명세서 (관리자 권한 미필요 API)

본 문서는 `_93-merge-requests` 디렉토리 내의 GitLab Merge Requests (머지 리퀘스트 목록 조회, 생성, 수정, 삭제, Diff 변경사항 조회, 리뷰어 지정, MR 병합/리베이스 실행 및 CI 파이프라인 연동) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 37개)

---

## 17. Create a merge request [POST]

### 기본 정보

- **기능:** 프로젝트 저장소에 새로운 Merge Request(MR)를 생성한다.
- **Endpoint:** `POST /api/v4/projects/{id}/merge_requests`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

작업용 브랜치(`source_branch`)의 커밋 변경사항을 대상 브랜치(`target_branch`: 예 `main` 또는 `develop`)로 병합하기 위한 Merge Request를 작성합니다. 제목(`title`), 상세 설명(`description`), 담당자(`assignee_ids`), 리뷰어(`reviewer_ids`), 라벨(`labels`), 마일스톤(`milestone_id`), 병합 후 소스 브랜치 자동 삭제 여부(`remove_source_branch`)를 설정할 수 있습니다.

### Request

#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Body
| 필드 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `source_branch` | string | Y | - | 변경사항이 포함된 작업 브랜치명 | `feature/S15P11A502-123` |
| `target_branch` | string | Y | - | 병합할 대상 기준 브랜치명 | `main` |
| `title` | string | Y | - | Merge Request 제목 | `[S15P11A502-123] feat: add user authentication API` |
| `description` | string | N | - | Markdown 형식의 상세 변경 설명 | `## 작업 내용\n- JWT 토큰 생성 및 검증 API 구현` |
| `assignee_ids` | array | N | - | 담당자 유저 ID 목록 | `[12]` |
| `reviewer_ids` | array | N | - | 코드 리뷰어 유저 ID 목록 | `[15, 18]` |
| `remove_source_branch` | boolean | N | `false` | 병합 완료 시 소스 브랜치 자동 삭제 여부 | `true` |

```json
{
  "source_branch": "feature/S15P11A502-123",
  "target_branch": "main",
  "title": "[S15P11A502-123] feat: add user authentication API",
  "description": "## 작업 내용\n- JWT 토큰 생성 및 검증 API 구현",
  "assignee_ids": [12],
  "reviewer_ids": [15, 18],
  "remove_source_branch": true
}
```

### Response

#### `201 Created`
```json
{
  "id": 105,
  "iid": 18,
  "project_id": 1234,
  "title": "[S15P11A502-123] feat: add user authentication API",
  "state": "opened",
  "source_branch": "feature/S15P11A502-123",
  "target_branch": "main",
  "merge_status": "can_be_merged",
  "web_url": "https://lab.ssafy.com/my-org/my-project/-/merge_requests/18"
}
```

---

## 32. Merge a merge request [PUT]

### 기본 정보

- **기능:** 검토가 완료된 Merge Request를 대상 브랜치에 병합(Merge) 실행한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/merge`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상, 보호 브랜치는 Maintainer/Owner)

### 설명

MR의 소스 브랜치 커밋들을 타깃 브랜치로 최종 병합합니다. `merge_when_pipeline_succeeds=true`로 설정하면 CI 파이프라인 성공 시 자동으로 병합되도록 예약할 수 있으며, `should_remove_source_branch` 옵션을 지정할 수 있습니다.

### Request

#### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `merge_request_iid` | integer | Y | MR 내부 번호 (IID) | `18` |

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `merge_commit_message` | string | N | 커스텀 머지 커밋 메시지 | `Merge branch 'feature/login' into 'main'` |
| `should_remove_source_branch` | boolean | N | 머지 시 소스 브랜치 삭제 여부 | `true` |
| `merge_when_pipeline_succeeds` | boolean | N | CI 통과 시 자동 머지 실행 여부 | `true` |

```json
{
  "should_remove_source_branch": true,
  "merge_when_pipeline_succeeds": true
}
```

### Response

#### `200 OK`
```json
{
  "id": 105,
  "iid": 18,
  "state": "merged",
  "merged_by": { "username": "kkh_ssafy" }
}
```

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

## 35. Rebase a merge request [PUT]

### 기본 정보

- **기능:** Target 브랜치의 최신 커밋 위로 MR 소스 브랜치를 리베이스(Rebase)한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/rebase`
- **인증:** Bearer Token 필요

---

## 09, 10. Global & Group Merge Requests (GET, GET)

- **Endpoints:**
  - `GET /api/v4/merge_requests`: 접근 가능한 전체 프로젝트 통합 MR 목록 조회
  - `GET /api/v4/groups/{id}/merge_requests`: 특정 그룹 범위 내 모든 MR 목록 조회
