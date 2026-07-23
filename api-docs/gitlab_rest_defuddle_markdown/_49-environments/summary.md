# Environments API 명세서 (관리자 권한 미필요 API)

본 문서는 `_49-environments` 디렉토리 내의 GitLab Environments (프로젝트 배포 환경: production, staging, review apps 관리 및 중지) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer, Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 8개)

---

## 01. List all environments [GET]

### 기본 정보

- **기능:** 프로젝트에 등록된 모든 배포 환경(Environment) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/environments`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트의 CI/CD 배포 대상 환경(예: `production`, `staging`, `testing`) 목록과 각 환경별 상태(`available`, `stopping`, `stopped`), 외부 접속 URL(`external_url`), 최신 배포 기록(`last_deployment`)을 조회합니다. `states` 파라미터로 특정 상태의 환경만 필터링할 수 있습니다.

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
| `name` | string | N | - | 특정 환경 이름 정확한 매칭 | `production` |
| `search` | string | N | - | 환경 이름 검색어 (3자 이상) | `prod` |
| `states` | string | N | - | 상태 필터 (`available` \| `stopping` \| `stopped`) | `available` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 환경 ID | `10` |
| `name` | string | 환경 이름 | `production` |
| `slug` | string | URL용 고유 식별자 슬러그 | `production` |
| `external_url` | string | 배포 서비스 외부 접속 URL | `https://a502.ssafy.io` |
| `state` | string | 환경 상태 (`available` \| `stopped`) | `available` |
| `tier` | string | 환경 티어 (`production` \| `staging` \| `testing` \| `development`) | `production` |
| `last_deployment` | object | 최신 배포 상세 정보 | `{ "id": 50, "sha": "a1b2c3...", "status": "success" }` |

```json
[
  {
    "id": 10,
    "name": "production",
    "slug": "production",
    "external_url": "https://a502.ssafy.io",
    "created_at": "2026-07-23T10:00:00Z",
    "tier": "production",
    "state": "available",
    "last_deployment": {
      "id": 50,
      "iid": 1,
      "ref": "main",
      "sha": "a1b2c3d4e5f6...",
      "status": "success"
    }
  }
]
```

---

## 02. Create an environment [POST]

### 기본 정보

- **기능:** 프로젝트에 신규 배포 환경을 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/environments`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

새로운 배포 환경 이름(`name`), 외부 접속 URL(`external_url`), 티어 종류(`tier`: `production`, `staging`, `testing`, `development`, `other`), 자동 중지 시각(`auto_stop_at`) 등을 설정하여 배포 대상 환경을 등록합니다. SSAFY 프로젝트 EC2 서버 및 도메인 연동 시 활용됩니다.

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

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 배포 환경 이름 | `production` |
| `external_url` | string | N | - | 배포된 서비스의 외부 접속 URL | `https://a502.ssafy.io` |
| `tier` | string | N | - | 환경 구분 티어 (`production` \| `staging` \| `testing` \| `development` \| `other`) | `production` |
| `description` | string | N | - | 환경에 대한 상세 설명 | `SSAFY EC2 Production Server` |

```json
{
  "name": "production",
  "external_url": "https://a502.ssafy.io",
  "tier": "production",
  "description": "SSAFY EC2 Main Production Server"
}
```

### Response

#### `201 Created`

```json
{
  "id": 10,
  "name": "production",
  "slug": "production",
  "external_url": "https://a502.ssafy.io",
  "tier": "production",
  "state": "available"
}
```

---

## 03. Update an existing environment [PUT]

### 기본 정보

- **기능:** 기존 배포 환경의 이름, 외부 URL, 설명 등의 설정을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/environments/{environment_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)


## 05. Retrieve an environment [GET]

### 기본 정보

- **기능:** 단일 배포 환경의 상세 정보 및 최신 배포 내역을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/environments/{environment_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)


```
