# Merge Request Approvals API 명세서 (관리자 권한 미필요 API)

본 문서는 `_92-merge-request-approvals` 디렉토리 내의 GitLab Merge Request Approvals (코드 리뷰 승인 규칙, 승인 상태 및 승인/승인 취소 처리) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 15개)

---

## 12. Approve merge request [POST]

### 기본 정보

- **기능:** 지정한 Merge Request에 승인(Approve)을 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approve`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상, 지정 승인권자)

### 설명

코드 리뷰어가 Merge Request를 검토한 후 승인(Approve)을 부여합니다. `sha` 파라미터를 지정하여 리뷰어가 확인한 특정 커밋 해시 버전과 현재 MR의 Head 커밋이 일치할 때만 안전하게 승인되도록 보호할 수 있습니다.

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
| `merge_request_iid` | integer | Y | Merge Request 내부 번호 (IID) | `15` |

#### Body
| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `sha` | string | N | 검토한 MR의 Head 커밋 SHA | `a1b2c3d4e5f6...` |
| `approval_password` | string | N | 승인에 비밀번호 재확인이 필요한 경우 입력 | `my-password` |

```json
{
  "sha": "a1b2c3d4e5f6..."
}
```

### Response

#### `201 Created`
```json
{
  "id": 102,
  "iid": 15,
  "project_id": 1234,
  "title": "Resolve user login API issue",
  "approved": true,
  "approvals_required": 2,
  "approvals_left": 0,
  "approved_by": [
    {
      "user": {
        "id": 12,
        "username": "kkh_ssafy",
        "name": "강기후"
      }
    }
  ]
}
```

---

## 13. Unapprove a merge request [POST]

### 기본 정보

- **기능:** 이미 부여한 Merge Request 승인(Approve) 상태를 취소(Unapprove)한다.
- **Endpoint:** `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/unapprove`
- **인증:** Bearer Token 필요
- **권한:** 해당 MR을 이전에 승인한 사용자 본인

---

## 10. Retrieve approval state for a merge request [GET]

### 기본 정보

- **기능:** 특정 Merge Request의 현재 승인 상태 및 적용된 규칙별 승인 수 현황을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_state`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

---

## 01 ~ 05. Merge Request Approval Rules (GET, POST, GET, PUT, DEL)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules`: MR에 적용된 승인 규칙 목록 조회
  - `POST /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules`: MR 개별 승인 규칙 추가 (`name`, `approvals_required`, `user_ids`, `group_ids`)
  - `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules/{rule_id}`: 단일 승인 규칙 상세 조회
  - `PUT /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules/{rule_id}`: 승인 규칙 수정 (필수 승인 수 `approvals_required` 변경)
  - `DELETE /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_rules/{rule_id}`: 승인 규칙 삭제

---

## 06 ~ 09. Project & Group Approval Settings (GET, PUT/POST)

- **Endpoints:**
  - `GET /api/v4/projects/{id}/approvals`: 프로젝트 전체 기본 MR 승인 정책 조회
  - `POST /api/v4/projects/{id}/approvals`: 프로젝트 기본 MR 승인 정책 설정 (`approvals_before_merge`, `reset_approvals_on_push`)
  - `GET /api/v4/groups/{id}/approvals`: 그룹 기본 MR 승인 정책 조회
  - `POST /api/v4/groups/{id}/approvals`: 그룹 기본 MR 승인 정책 설정
