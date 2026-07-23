# Protected Branches API 명세서 (관리자 권한 미필요 API)

본 문서는 `_131-protected-branches` 디렉토리 내의 GitLab Protected Branches (보호된 브랜치 관리) 관련 API 중 일반 프로젝트/그룹 관리자(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 10개)

---

## 01. List all protected branches for a group [GET]

### 기본 정보

- **기능:** 특정 그룹 레벨에 설정된 보호된 브랜치(Protected Branch) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/protected_branches`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Developer 이상)

### 설명

그룹 수준에서 상속 및 설정된 모든 보호 브랜치 규칙 목록을 조회합니다. 와일드카드 브랜치 규칙이 있는 경우 해당 와일드카드 표현식을 포함하여 반환합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩된 경로 | `my-org` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | N | - | 브랜치 이름 검색어 | `main` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 보호 브랜치 규칙 ID | `1` |
| `name` | string | 브랜치 이름 또는 와일드카드 패턴 | `main` |
| `push_access_levels` | array | 푸시 권한 레벨 정보 배열 | `[ { "access_level": 40, "access_level_description": "Maintainers" } ]` |
| `merge_access_levels` | array | 머지 권한 레벨 정보 배열 | `[ { "access_level": 30, "access_level_description": "Developers + Maintainers" } ]` |
| `allow_force_push` | boolean | 강제 푸시 허용 여부 | `false` |

```json
[
  {
    "id": 1,
    "name": "main",
    "push_access_levels": [
      {
        "access_level": 40,
        "access_level_description": "Maintainers"
      }
    ],
    "merge_access_levels": [
      {
        "access_level": 30,
        "access_level_description": "Developers + Maintainers"
      }
    ],
    "allow_force_push": false,
    "code_owner_approval_required": false
  }
]
```

---


## 06. List all protected branches for a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트에 설정된 모든 보호된 브랜치 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/protected_branches`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

프로젝트에 설정된 브랜치 보호 규칙(main, release/* 등) 목록을 가져옵니다. 각 브랜치별 머지 권한, 푸시 권한, 코드 오너 승인 요구 여부, 상속 여부(`inherited`)를 포함합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | N | - | 보호 브랜치 이름 검색어 | `release` |

#### Body

없음

### Response

#### `200 OK`

```json
[
  {
    "id": 10,
    "name": "main",
    "push_access_levels": [
      {
        "access_level": 40,
        "access_level_description": "Maintainers"
      }
    ],
    "merge_access_levels": [
      {
        "access_level": 30,
        "access_level_description": "Developers + Maintainers"
      }
    ],
    "allow_force_push": false,
    "code_owner_approval_required": true,
    "inherited": false
  }
]
```

---

## 07. Protect repository branches for a project [POST]

### 기본 정보

- **기능:** 프로젝트의 특정 브랜치 또는 와일드카드 브랜치를 보호 브랜치로 설정한다.
- **Endpoint:** `POST /api/v4/projects/{id}/protected_branches`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### 설명

프로젝트의 특정 브랜치(예: `main`, `develop`, `release/*`)를 보호 브랜치로 지정을 요청합니다. 푸시 및 머지를 허용할 권한 레벨(`push_access_level`, `merge_access_level`)과 Code Owner 승인 필수 여부(`code_owner_approval_required`)를 설정할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 보호할 브랜치 이름 또는 와일드카드 | `main` |
| `push_access_level` | integer | N | `40` | 푸시 권한 레벨 (`0` No access, `30` Developer, `40` Maintainer) | `40` |
| `merge_access_level` | integer | N | `45` | 머지 권한 레벨 (`30` Developer, `40` Maintainer) | `30` |
| `allow_force_push` | boolean | N | `false` | 강제 푸시 허용 여부 | `false` |
| `code_owner_approval_required` | boolean | N | `false` | Code Owners 승인 필수 여부 | `true` |

```json
{
  "name": "main",
  "push_access_level": 40,
  "merge_access_level": 30,
  "allow_force_push": false,
  "code_owner_approval_required": true
}
```

### Response

#### `201 Created`

```json
{
  "id": 10,
  "name": "main",
  "allow_force_push": false,
  "code_owner_approval_required": true
}
```

---

## 08. Retrieve a protected branch or wildcard protected branch [GET]

### 기본 정보

- **기능:** 프로젝트의 단일 보호 브랜치 규칙 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/protected_branches/{name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 09. Update a protected branch for a project [PATCH]

### 기본 정보

- **기능:** 프로젝트의 보호 브랜치 권한 및 설정 규칙을 수정한다.
- **Endpoint:** `PATCH /api/v4/projects/{id}/protected_branches/{name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

---

## 10. Unprotect repository branches for a project [DEL]

### 기본 정보

- **기능:** 프로젝트의 브랜치 보호 설정을 해제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/protected_branches/{name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Response

#### `204 No Content`
성공 시 본문 없이 `204 No Content`를 반환합니다.
