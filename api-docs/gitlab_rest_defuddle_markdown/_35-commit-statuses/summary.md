# Commit Statuses API 명세서 (관리자 권한 미필요 API)

본 문서는 `_35-commit-statuses` 디렉토리 내의 GitLab Commit Statuses (외부 빌드/CI 도구와 연동하여 특정 커밋의 파이프라인 빌드 상태 조회 및 업데이트) 관련 API 중 일반 사용자 및 프로젝트 멤버(Developer 이상) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 2개)

---

## 01. List all commit statuses [GET]

### 기본 정보

- **기능:** 특정 커밋 SHA에 대한 모든 파이프라인/빌드 상태(Status) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/commits/{sha}/statuses`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

지정한 프로젝트의 특정 커밋(`sha`)에 결합된 파이프라인 잡 및 외부 CI 시스템의 실행 상태(`pending`, `running`, `success`, `failed`, `canceled`, `skipped`) 목록을 가져옵니다. `all=true` 옵션을 설정하면 최신 상태 외 과거의 전체 빌드 상태 이력을 포함하여 반환합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| item | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |
| `sha` | string | Y | 프로젝트의 커밋 해시 (SHA-1 / SHA-256) | `a1b2c3d4e5f6...` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `ref` | string | N | default branch | 대상 브랜치명 또는 태그명 | `main` |
| `stage` | string | N | - | 빌드 스테이지 필터 (`build` \| `test` \| `deploy`) | `test` |
| `name` | string | N | - | 잡(Job) 이름 필터 | `jenkins-build` |
| `pipeline_id` | integer | N | - | 파이프라인 ID 필터 | `567` |
| `all` | boolean | N | `false` | 최신 상태만(false) 또는 전체 히스토리 포함(true) | `false` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 상태 객체 ID | `890` |
| `sha` | string | 대상 커밋 SHA | `a1b2c3d4e5f6...` |
| `ref` | string | 브랜치명 | `main` |
| `status` | string | 빌드 상태 (`pending`, `running`, `success`, `failed`) | `success` |
| `name` | string | 빌드/잡 구분 이름 | `jenkins/build` |
| `target_url` | string | 외부 CI 도구(Jenkins 등) 결과 상세 페이지 URL | `https://jenkins.example.com/job/my-app/12/` |
| `coverage` | number | 코드 커버리지 수치 (%) | `85.5` |

```json
[
  {
    "id": 890,
    "sha": "a1b2c3d4e5f6...",
    "ref": "main",
    "status": "success",
    "name": "jenkins/build",
    "target_url": "https://jenkins.example.com/job/my-app/12/",
    "description": "Jenkins build succeeded",
    "created_at": "2026-07-23T10:00:00Z",
    "started_at": "2026-07-23T10:00:05Z",
    "finished_at": "2026-07-23T10:02:30Z",
    "allow_failure": false,
    "coverage": 85.5,
    "pipeline_id": 567
  }
]
```

---

## 02. Create or update a commit pipeline status [POST]

### 기본 정보

- **기능:** 외부 CI 도구(Jenkins 등)에서 특정 커밋의 파이프라인 빌드 상태를 등록하거나 업데이트한다.
- **Endpoint:** `POST /api/v4/projects/{id}/statuses/{sha}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

외부 젠킨스(Jenkins) 또는 타 CI 도구에서 빌드 결과를 GitLab 프로젝트 커밋 상에 전송하여 커밋 빌드 상태(`state`) 및 외부 링크(`target_url`), 결과 설명(`description`), 커버리지 수치(`coverage`)를 반영시킵니다. SSAFY 환경에서 EC2 t3.xlarge에 호스팅된 Jenkins에서 빌드 후 GitLab 커밋 상태를 갱신할 때 필수적으로 사용됩니다.

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
| `sha` | string | Y | 대상 커밋 SHA | `a1b2c3d4e5f6...` |

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `state` | string | Y | `pending` \| `running` \| `success` \| `failed` \| `canceled` \| `skipped` | 상태값 | `success` |
| `ref` | string | N | - | 브랜치 또는 태그명 | `main` |
| `target_url` | string | N | - | 클릭 시 이동할 외부 CI(Jenkins) 빌드 URL | `https://jenkins.ssafy.com/job/A502/15` |
| `description` | string | N | - | 상태에 대한 간략한 설명 | `Jenkins build #15 succeeded` |
| `name` | string | N | - | 빌드 구분 식별 라벨 (기본값: `default`) | `jenkins/build` |
| `context` | string | N | - | 상태 구분을 위한 컴포넌트 라벨 | `continuous-integration/jenkins` |
| `coverage` | number | N | - | 코드 커버리지 백분율 | `88.5` |
| `pipeline_id` | integer | N | - | 연결할 GitLab 파이프라인 ID | `567` |

```json
{
  "state": "success",
  "ref": "main",
  "name": "jenkins/build",
  "target_url": "https://jenkins.ssafy.com/job/A502/15",
  "description": "Jenkins build #15 succeeded",
  "coverage": 88.5
}
```

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 파이프라인 상태 ID | `891` |
| `sha` | string | 커밋 SHA | `a1b2c3d4e5f6...` |
| `status` | string | 설정된 상태 | `success` |
| `target_url` | string | 외부 CI 결과 URL | `https://jenkins.ssafy.com/job/A502/15` |

```json
{
  "id": 891,
  "sha": "a1b2c3d4e5f6...",
  "ref": "main",
  "status": "success",
  "name": "jenkins/build",
  "target_url": "https://jenkins.ssafy.com/job/A502/15",
  "description": "Jenkins build #15 succeeded",
  "created_at": "2026-07-23T10:05:00Z",
  "finished_at": "2026-07-23T10:07:30Z",
  "coverage": 88.5
}
```
