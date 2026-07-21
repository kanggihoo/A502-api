# Approval Rules API Spec

## 01-Get all project approval rules [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 approval rule 조회 (Private API, 변경 가능)
- **Endpoint:** `GET /api/v4/projects/{id}/approval_settings`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 approval rule과 fallback approvals required 값을 반환합니다. 이 API는 Private API로 예고 없이 변경될 수 있습니다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `target_branch` | string | N | approval rule이 적용되는 브랜치 범위 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `rules[]` | array | approval rule 목록 |
| `rules[].id` | integer | rule ID |
| `rules[].name` | string | rule 이름 |
| `rules[].rule_type` | string | rule 유형 |
| `rules[].approvals_required` | integer | 필요한 승인 수 |
| `rules[].users[]` | array | 지정된 승인자 목록 |
| `rules[].users[].id` | integer | 사용자 ID |
| `rules[].users[].username` | string | 사용자명 |
| `rules[].users[].name` | string | 이름 |
| `rules[].users[].state` | string | 상태 (active/blocked) |
| `rules[].users[].avatar_url` | string | 아바타 URL |
| `rules[].users[].web_url` | string | 프로필 URL |
| `rules[].groups[]` | array | 지정된 그룹 목록 |
| `rules[].groups[].id` | integer | 그룹 ID |
| `rules[].groups[].name` | string | 그룹 이름 |
| `rules[].groups[].full_path` | string | 전체 경로 |
| `rules[].contains_hidden_groups` | boolean | 숨겨진 그룹 포함 여부 |
| `rules[].report_type` | string | 보고서 유형 (license_scanning, code_coverage 등) |
| `rules[].protected_branches[]` | array | 보호 브랜치 설정 |
| `rules[].applies_to_all_protected_branches` | boolean | 모든 보호 브랜치 적용 여부 |
| `rules[].coverage_minimum_threshold` | number | 최소 커버리지 임계값 |
| `rules[].scanners[]` | array | 스캐너 목록 |
| `rules[].vulnerabilities_allowed` | integer | 허용된 취약점 수 |
| `rules[].severity_levels[]` | array | 심각도 수준 목록 |
| `rules[].vulnerability_states[]` | array | 취약점 상태 목록 |
| `rules[].approvers[]` | array | 승인자 목록 |
| `fallback_approvals_required` | integer | 폴백 승인 필요 수 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |

---

## 05-List all approval rules for a group [GET]

## 기본 정보
- **기능:** 그룹의 모든 approval rule 목록 조회
- **Endpoint:** `GET /api/v4/groups/{id}/approval_rules`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET), 그룹 관리자로 제한됨
- **멱등성:** GET은 지원

## 설명
지정된 그룹의 모든 approval rule과 관련 상세 정보를 반환합니다. 그룹 관리자만 접근 가능합니다. 페이지네이션 지원 (`page`, `per_page`).

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | string | Y | 그룹 ID |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | rule ID |
| `name` | string | rule 이름 |
| `rule_type` | string | rule 유형 (regular, report_approver, code_owner 등) |
| `eligible_approvers[]` | array | 승인 가능한 사용자 목록 |
| `eligible_approvers[].id` | integer | 사용자 ID |
| `eligible_approvers[].username` | string | 사용자명 |
| `eligible_approvers[].name` | string | 이름 |
| `eligible_approvers[].state` | string | 상태 |
| `approvals_required` | integer | 필요한 승인 수 |
| `users[]` | array | 지정된 승인자 목록 |
| `groups[]` | array | 지정된 그룹 목록 |
| `contains_hidden_groups` | boolean | 숨겨진 그룹 포함 여부 |
| `report_type` | string | 보고서 유형 |
| `protected_branches[]` | array | 보호 브랜치 설정 |
| `applies_to_all_protected_branches` | boolean | 모든 보호 브랜치 적용 여부 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |

---

## 08-List all approval rules for a project [GET]

## 기본 정보
- **기능:** 프로젝트의 모든 approval rule 목록 조회
- **Endpoint:** `GET /api/v4/projects/{id}/approval_rules`
- **인증:** Bearer Token 필요
- **권한:** `read_api` (GET)
- **멱등성:** GET은 지원

## 설명
지정된 프로젝트의 모든 approval rule과 관련 상세 정보를 반환합니다. 페이지네이션 지원 (`page`, `per_page`).

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | integer | rule ID |
| `name` | string | rule 이름 |
| `rule_type` | string | rule 유형 (regular, report_approver, code_owner 등) |
| `eligible_approvers[]` | array | 승인 가능한 사용자 목록 |
| `eligible_approvers[].id` | integer | 사용자 ID |
| `eligible_approvers[].username` | string | 사용자명 |
| `eligible_approvers[].name` | string | 이름 |
| `eligible_approvers[].state` | string | 상태 |
| `approvals_required` | integer | 필요한 승인 수 |
| `users[]` | array | 지정된 승인자 목록 |
| `groups[]` | array | 지정된 그룹 목록 |
| `contains_hidden_groups` | boolean | 숨겨진 그룹 포함 여부 |
| `report_type` | string | 보고서 유형 |
| `protected_branches[]` | array | 보호 브랜치 설정 |
| `applies_to_all_protected_branches` | boolean | 모든 보호 브랜치 적용 여부 |
| `coverage_minimum_threshold` | number | 최소 커버리지 임계값 |

## Errors
| 상태 | 설명 |
|---|---:|
| 400 | Bad Request |
| 404 | Not Found |
