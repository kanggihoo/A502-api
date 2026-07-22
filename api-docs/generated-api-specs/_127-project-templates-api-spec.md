# 127-project-templates — 프로젝트 템플릿 API

프로젝트 템플릿 후보를 조회한다.
**`main` 브랜치 버전 기준 템플릿이 적용됨.**

### 동작 방식
- `develop`에서 템플릿 내용을 아무리 바꿔도, **`main` 브랜치에 머지되기 전까지는 `main`의 구 버전 템플릿이 불러와짐**.
- GitLab 템플릿 시스템은 **100% Default Branch (`main`)의 파일 내용만 참조함**.

---

### 결론
- 템플릿 추가/수정/삭제 후 즉시 적용하려면 **`main` 브랜치로 반영(Merge) 필요**.
---

## 01 — List all templates of a particular type [GET]

### 기본 정보
- **기능:** 프로젝트에서 특정 유형의 템플릿 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/templates/{type}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에서 특정 유형( Dockerfile, .gitignore, GitLab CI YAML, 라이선스, 이슈 템플릿, MR 템플릿)의 템플릿 목록을 반환한다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL 인코딩된 경로 |
| `type` | string | Y | 템플릿 유형 (`dockerfiles` / `gitignores` / `gitlab_ci_ymls` / `licenses` / `issues` / `merge_requests`) |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `key` | string | 템플릿 키 식별자 | `python` |
| `name` | string | 템플릿 표시 이름 | `Python` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 401 | 인증 실패 |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 연동 참고사항

- 템플릿 유형별로 인스턴스에 내장된 기본 템플릿 목록이 반환된다.
- 개별 템플릿의 상세 내용은 `GET /projects/{id}/templates/{type}/{key}`로 조회한다.
- 프로젝트 시작 시 `.gitignore`, `GitLab CI YAML`, `라이선스` 템플릿을 조합하여 초기 설정을 자동화할 수 있다.
- 이슈/MR 템플릿(`issues`, `merge_requests`)은 프로젝트 내 `.gitlab/issue_templates/`, `.gitlab/merge_request_templates/` 디렉터리에 저장된 커스텀 템플릿도 포함한다.
