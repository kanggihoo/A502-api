# Analytics API 명세서 (관리자 권한 미필요 API)

본 문서는 `_10-analytics` 디렉토리 내의 GitLab Analytics 관련 API 중 일반 사용자/프로젝트 멤버/그룹 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 7개)

---

## 01. List deployment frequencies for the project [GET]

### 기본 정보

- **기능:** 프로젝트의 배포 빈도(Deployment Frequency) 분석 데이터를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/analytics/deployment_frequency`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

지정한 프로젝트의 특정 환경(`environment`)에 대해 특정 기간 동안 수행된 배포 빈도를 조회합니다. 시작 일시(`from`) 지정은 필수이며, 종료 일시(`to`) 및 집계 주기(`interval`)를 옵션으로 지정하여 배포 통계 데이터를 가져올 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1234` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `environment` | string | Y | - | 필터링할 환경 이름 | `production` |
| `from` | string | Y | - | 데이터 조회 시작 일시 (포함, ISO 8601) | `2026-01-01T00:00:00Z` |
| `to` | string | N | - | 데이터 조회 종료 일시 (미포함, ISO 8601) | `2026-07-01T00:00:00Z` |
| `interval` | string | N | - | 데이터 롤업 집계 주기 (예: `all`, `monthly`, `daily`) | `daily` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `value` | string | 배포 빈도 수치 | `12` |
| `from` | string | 집계 시작 일시 | `2026-01-01T00:00:00Z` |
| `to` | string | 집계 종료 일시 | `2026-07-01T00:00:00Z` |

```json
{
  "value": "12",
  "from": "2026-01-01T00:00:00Z",
  "to": "2026-07-01T00:00:00Z"
}
```

---

### 기본 정보

- **기능:** 지정한 그룹 내에서 최근에 생성된 이슈(Issue) 개수를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/group_activity/issues_count`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Reporter 이상)

### 설명

지정한 그룹 경로(`group_path`)에 대해 최근 생성된 이슈의 전체 개수를 가져옵니다. 그룹의 최근 이슈 생성 활동성을 한눈에 파악할 수 있으며, 조회 결과 개수는 최대 1000개로 제한됩니다.

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
| `group_path` | string | Y | - | 대상 그룹 경로 | `my-org/my-group` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `issues_count` | integer | 최근 생성된 이슈 수 (최대 1,000개 제한) | `42` |

```json
{
  "issues_count": 42
}
```

---

## 06. Retrieve count of recently created merge requests for a group [GET]

### 기본 정보

- **기능:** 지정한 그룹 내에서 최근에 생성된 머지 리퀘스트(MR) 개수를 조회한다.
- **Endpoint:** `GET /api/v4/analytics/group_activity/merge_requests_count`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Reporter 이상)

### 설명

지정한 그룹 경로(`group_path`) 내에서 최근 새로 작성된 Merge Request의 총 수량을 조회합니다. 개발 및 리뷰 활동 빈도를 파악할 때 유용하며, 반환되는 개수는 최대 1000개로 제한됩니다.

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
| `group_path` | string | Y | - | 대상 그룹 경로 | `my-org/my-group` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `merge_requests_count` | integer | 최근 생성된 머지 리퀘스트 수 (최대 1,000개 제한) | `18` |

```json
{
  "merge_requests_count": 18
}
```

---


