# 73-invitations — 초대(Invitation) API

그룹·프로젝트 초대의 대기·수락 전 단계를 다룬다.

---

## 02 — List all pending invitations for a group [GET]

### 기본 정보
- **기능:** 그룹의 모든 대기 중인 초대 목록을 조회한다
- **Endpoint:** `GET /api/v4/groups/{id}/invitations`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 그룹에 대해 현재 인증된 사용자가 볼 수 있는 모든 대기 중인 초대를 반환한다. 직접 멤버 초대만 포함하며, 상위 그룹에서 상속된 초대는 포함하지 않는다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | string | Y | 그룹 ID |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `query` | string | N | 멤버 검색어 |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `access_level` | string | 초대된 접근 권한 수준 | `developer` |
| `created_at` | string | 초대 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `expires_at` | string | 초대 만료 일시 | `2024-02-01T00:00:00Z` |
| `invite_email` | string | 초대받은 이메일 주소 | `user@example.com` |
| `invite_token` | string | 초대 토큰 | `abc123` |
| `user_name` | string | 초대받은 사용자 이름 (미등록 시 null) | `null` |
| `created_by_name` | string | 초대를 보낸 사용자 이름 | `Admin User` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 404 | 그룹을 찾을 수 없음 |

---

## 06 — List all pending invitations for a project [GET]

### 기본 정보
- **기능:** 프로젝트의 모든 대기 중인 초대 목록을 조회한다
- **Endpoint:** `GET /api/v4/projects/{id}/invitations`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

### 설명
지정된 프로젝트에 대해 현재 인증된 사용자가 볼 수 있는 모든 대기 중인 초대를 반환한다. 직접 멤버 초대만 포함하며, 상위 그룹에서 상속된 초대는 포함하지 않는다.

### Request
#### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID |

#### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|---|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `query` | string | N | 멤버 검색어 |

### Response
#### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|---|
| `access_level` | string | 초대된 접근 권한 수준 | `developer` |
| `created_at` | string | 초대 생성 일시 (ISO 8601) | `2024-01-01T00:00:00Z` |
| `expires_at` | string | 초대 만료 일시 | `2024-02-01T00:00:00Z` |
| `invite_email` | string | 초대받은 이메일 주소 | `user@example.com` |
| `invite_token` | string | 초대 토큰 | `abc123` |
| `user_name` | string | 초대받은 사용자 이름 (미등록 시 null) | `null` |
| `created_by_name` | string | 초대를 보낸 사용자 이름 | `Admin User` |

### Errors
| 상태 코드 | 설명 |
|---|---:|---|
| 400 | 잘못된 요청 |
| 404 | 프로젝트를 찾을 수 없음 |

---

## 연동 참고사항

- 초대는 아직 수락되지 않은 상태의 pending invitation만 조회된다.
- 초대를 수락하면 멤버십(members) API 영역으로 이동한다.
- `query` 파라미터로 이메일 주소나 사용자 이름을 부분 검색할 수 있다.
- 초대를 보내는 작업은 `POST /groups/{id}/invitations` 또는 `POST /projects/{id}/invitations`를 사용한다 (POC 이후 확장).
