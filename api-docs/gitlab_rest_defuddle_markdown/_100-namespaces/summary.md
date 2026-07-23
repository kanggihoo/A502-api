# Namespaces API 명세서 (관리자 권한 미필요 API)



## 01. Retrieve namespace subscription [GET]

### 기본 정보

- **기능:** 특정 네임스페이스의 GitLab 구독(Subscription) 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/namespaces/{id}/gitlab_subscription`
- **인증:** Bearer Token 필요
- **권한:** Namespace Owner / 해당 네임스페이스 멤버

### 설명

지정한 네임스페이스의 플랜(Plan), 사용량(Usage), 청구(Billing) 정보 등 GitLab 구독 상세 내역을 조회합니다. 네임스페이스의 구독 요금제 상태나 할당량 사용 현황을 확인하는 데 사용됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 네임스페이스 ID 또는 URL 인코딩된 경로 | `1234` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `plan` | object | 요금제 플랜 정보 | `{ "code": "ultimate", "name": "Ultimate" }` |
| `usage` | object | 리소스 사용량 정보 | `{ "seats_in_use": 10 }` |
| `billing` | object | 청구 관련 정보 | `{ "pay_method": "credit_card" }` |

```json
{
  "plan": {
    "code": "ultimate",
    "name": "Ultimate"
  },
  "usage": {
    "seats_in_use": 10
  },
  "billing": {
    "pay_method": "credit_card"
  }
}
```

---


## 03. Retrieve namespace details [GET]

### 기본 정보

- **기능:** 특정 네임스페이스의 상세 정보(이름, 경로, 프로젝트 수, 멤버 수 등)를 조회한다.
- **Endpoint:** `GET /api/v4/namespaces/{id}`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자 (해당 네임스페이스 조회가 허용된 사용자)

### 설명

네임스페이스 ID 또는 URL 인코딩된 경로를 통해 네임스페이스의 기본 정보(이름, path, kind, web_url), 포함된 프로젝트 수, 멤버 수, 사용 중인 시트 수 등을 상세 조회합니다. 네임스페이스 식별 및 상태 파악 시 필수적으로 사용됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 네임스페이스 ID 또는 URL 인코딩 경로 | `my-org/my-namespace` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 네임스페이스 ID | `1234` |
| `name` | string | 네임스페이스 이름 | `My Namespace` |
| `path` | string | 네임스페이스 경로 | `my-namespace` |
| `kind` | string | 네임스페이스 종류 (`user` 또는 `group`) | `group` |
| `full_path` | string | 네임스페이스 전체 경로 | `my-org/my-namespace` |
| `web_url` | string | 웹 UI 접근 URL | `https://gitlab.com/groups/my-org/my-namespace` |
| `projects_count` | integer | 네임스페이스 내 프로젝트 수 | `5` |
| `members_count_with_descendants` | integer | 하위 항목 포함 총 멤버 수 | `12` |

```json
{
  "id": 1234,
  "name": "My Namespace",
  "path": "my-namespace",
  "kind": "group",
  "full_path": "my-org/my-namespace",
  "web_url": "https://gitlab.com/groups/my-org/my-namespace",
  "projects_count": 5,
  "members_count_with_descendants": 12
}
```

---

## 04. List all namespaces [GET]

### 기본 정보

- **기능:** 현재 인증된 사용자가 접근 가능한 모든 네임스페이스 목록을 조회한다.
- **Endpoint:** `GET /api/v4/namespaces`
- **인증:** Bearer Token 필요
- **권한:** 인증된 사용자 (일반 사용자는 본인이 접근 권한을 가진 네임스페이스 목록 조회, 관리자는 전역 조회)

### 설명

사용자가 접근할 권한이 있는 사용자(user) 및 그룹(group) 네임스페이스 목록을 반환합니다. 검색어(`search`), 소유한 네임스페이스만 필터링(`owned_only`), 최상위 네임스페이스만 조회(`top_level_only`) 등 다양한 검색 및 페이지네이션 옵션을 제공합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

없음

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `search` | string | N | - | 네임스페이스 이름 또는 경로 검색어 | `my-team` |
| `owned_only` | boolean | N | - | 직접 소유한 네임스페이스만 반환 여부 | `true` |
| `top_level_only` | boolean | N | - | 최상위(Top-level) 네임스페이스만 포함 여부 | `true` |
| `full_path_search` | boolean | N | - | `search` 검색 시 전체 경로(full path) 매칭 여부 | `true` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |
| `requested_hosted_plan` | string | N | - | 요청된 호스팅 플랜 이름 | `ultimate` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 네임스페이스 ID | `1234` |
| `name` | string | 네임스페이스 이름 | `My Team` |
| `path` | string | 네임스페이스 경로 | `my-team` |
| `kind` | string | 네임스페이스 종류 (`user` / `group`) | `group` |
| `full_path` | string | 전체 경로 | `my-team` |
| `web_url` | string | 웹 URL | `https://gitlab.com/groups/my-team` |

```json
[
  {
    "id": 1234,
    "name": "My Team",
    "path": "my-team",
    "kind": "group",
    "full_path": "my-team",
    "web_url": "https://gitlab.com/groups/my-team"
  }
]
```

---


