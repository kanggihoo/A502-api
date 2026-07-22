# Merge Request Approvals API Spec
Tier: Premium, Ultimate
## 06-Retrieve MR approval settings for a project [GET]

## 기본 정보
- **기능:** 프로젝트의 MR approval 설정 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_request_approval_setting`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 merge request approval 설정을 반환합니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `allow_author_approval` | boolean | 작성자 승인 허용 여부 |
| `allow_committer_approval` | boolean | 커미터 승인 허용 여부 |
| `allow_overrides_to_approver_list_per_merge_request` | boolean | MR별 승인자 목록 재정의 허용 여부 |
| `retain_approvals_on_push` | boolean | 푸시 시 승인 유지 여부 |
| `selective_code_owner_removals` | boolean | 선택적 코드 소유자 제거 여부 |
| `require_password_to_approve` | boolean | 승인 시 비밀번호 필요 여부 |
| `require_reauthentication_to_approve` | boolean | 승인 시 재인증 필요 여부 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 403 | Forbidden |
| 404 | Not Found |

---

## 10-Retrieve approval state for a merge request [GET]

## 기본 정보
- **기능:** MR의 승인 상태 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approvals`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 merge request의 승인 상태를 반환합니다. `approved_by`에는 approval rule 충족 여부와 관계없이 모든 승인자 정보가 포함됩니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | integer | Y | MR의 IID |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `user_has_approved` | boolean | 현재 사용자가 승인했는지 여부 |
| `user_can_approve` | boolean | 현재 사용자가 승인 가능한지 여부 |
| `approved` | boolean | MR이 승인되었는지 여부 |
| `approved_by.user` | object | 승인자 정보 |
| `approved_by.user.id` | integer | 사용자 ID |
| `approved_by.user.username` | string | 사용자명 |
| `approved_by.user.name` | string | 이름 |
| `approved_by.user.state` | string | 상태 |
| `approved_by.user.avatar_url` | string | 아바타 URL |
| `approved_by.user.web_url` | string | 프로필 URL |
| `approved_by.approved_at` | string | 승인 일시 |

## Errors
| 상태 | 설명 |
|---|---:|
| 404 | Not Found |

---

## 15-Retrieve approval details for a merge request [GET]

## 기본 정보
- **기능:** MR의 승인 상세 정보 조회
- **Endpoint:** `GET /api/v4/projects/{id}/merge_requests/{merge_request_iid}/approval_state`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 merge request의 승인 상세 정보를 반환합니다. 사용자가 MR의 approval rule을 수정한 경우 `approval_rules_overwritten`이 포함됩니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |
| `merge_request_iid` | integer | Y | MR의 IID |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `approval_rules_overwritten` | boolean | approval rule 재정의 여부 |
| `rules[]` | array | approval rule 상세 목록 |
| `rules[].id` | integer | rule ID |
| `rules[].name` | string | rule 이름 |
| `rules[].rule_type` | string | rule 유형 |
| `rules[].eligible_approvers[]` | array | 승인 가능한 사용자 목록 |
| `rules[].approvals_required` | integer | 필요한 승인 수 |
| `rules[].users[]` | array | 지정된 승인자 목록 |
| `rules[].groups[]` | array | 지정된 그룹 목록 |
| `rules[].contains_hidden_groups` | boolean | 숨겨진 그룹 포함 여부 |
| `rules[].report_type` | string | 보고서 유형 |
| `rules[].section` | string | 섹션 정보 |
| `rules[].source_rule` | object | 원본 rule 정보 (`approvals_required`) |
| `rules[].overridden` | boolean | 재정의 여부 |
| `rules[].code_owner` | boolean | code owner rule 여부 |
| `rules[].approved_by[]` | array | 승인한 사용자 목록 |
| `rules[].approved` | boolean | 해당 rule이 승인되었는지 여부 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |
