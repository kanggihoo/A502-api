# Badges API 명세서 (관리자 권한 미필요 API)

본 문서는 `_17-badges` 디렉토리 내의 GitLab Badges (그룹 및 프로젝트 상단의 파이프라인/배포 상태 뱃지 관리) 관련 API 중 일반 사용자 및 프로젝트/그룹 멤버(Maintainer, Owner) 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 12개)

---

## 01. List all badges for a group [GET]

### 기본 정보

- **기능:** 특정 그룹에 설정된 뱃지(Badge) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/badges`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Guest 이상)

### 설명

그룹에 등록된 파이프라인 빌드 상태, 커버리지 등의 뱃지 목록을 가져옵니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `my-group` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | N | - | 뱃지 이름 검색어 | `coverage` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 뱃지 ID | `1` |
| `name` | string | 뱃지 이름 | `Pipeline Status` |
| `link_url` | string | 뱃지 클릭 시 이동할 URL 패턴 | `https://gitlab.com/%{project_path}/-/commits/%{default_branch}` |
| `image_url` | string | 뱃지 이미지 URL 패턴 | `https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg` |
| `kind` | string | 뱃지 종류 (`group` \| `project`) | `group` |

```json
[
  {
    "id": 1,
    "name": "Pipeline Status",
    "link_url": "https://gitlab.com/%{project_path}/-/commits/%{default_branch}",
    "image_url": "https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg",
    "rendered_link_url": "https://gitlab.com/my-group/my-project/-/commits/main",
    "rendered_image_url": "https://gitlab.com/my-group/my-project/badges/main/pipeline.svg",
    "kind": "group"
  }
]
```

---

## 02. Create a badge for a group [POST]

### 기본 정보

- **기능:** 그룹에 새로운 뱃지를 추가한다.
- **Endpoint:** `POST /api/v4/groups/{id}/badges`
- **인증:** Bearer Token 필요
- **권한:** 그룹 Maintainer / Owner

### 설명

그룹 산하 프로젝트들에 표시될 뱃지를 등록합니다. 뱃지 이미지 URL(`image_url`)과 이동 링크 URL(`link_url`)에는 `%{project_path}`, `%{default_branch}`, `%{commit_sha}` 등 GitLab 변수를 사용할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |
| `Content-Type` | Y | 요청 형식 | `application/json` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID | `my-group` |

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `link_url` | string | Y | - | 뱃지 클릭 이동 URL 패턴 | `https://gitlab.com/%{project_path}/-/commits/%{default_branch}` |
| `image_url` | string | Y | - | 뱃지 SVG 이미지 URL 패턴 | `https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg` |
| `name` | string | N | - | 뱃지 이름 | `Pipeline Status` |

```json
{
  "name": "Pipeline Status",
  "link_url": "https://gitlab.com/%{project_path}/-/commits/%{default_branch}",
  "image_url": "https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg"
}
```

### Response

#### `201 Created`

```json
{
  "id": 1,
  "name": "Pipeline Status",
  "link_url": "https://gitlab.com/%{project_path}/-/commits/%{default_branch}",
  "image_url": "https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg",
  "kind": "group"
}
```

---

## 03. Retrieve a badge preview for a group [GET]

### 기본 정보

- **기능:** 그룹 뱃지 렌더링 미리보기 URL 결과를 반환한다.
- **Endpoint:** `GET /api/v4/groups/{id}/badges/render`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Guest 이상)

---

## 04. Retrieve a badge for a group [GET]

### 기본 정보

- **기능:** 그룹의 단일 뱃지 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요

---

## 05. Update a badge for a group [PUT]

### 기본 정보

- **기능:** 그룹 뱃지 정보(이름, 이미지 URL, 링크 URL)를 수정한다.
- **Endpoint:** `PUT /api/v4/groups/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요
- **권한:** 그룹 Maintainer / Owner

---

## 06. Delete a badge from a group [DEL]

### 기본 정보

- **기능:** 그룹 뱃지를 삭제한다.
- **Endpoint:** `DELETE /api/v4/groups/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요
- **권한:** 그룹 Maintainer / Owner

---

## 07. List all badges for a project [GET]

### 기본 정보

- **기능:** 특정 프로젝트에 설정된 뱃지 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/badges`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트의 README 및 메인 페이지에 표시되는 CI/CD 파라미터 뱃지, 커버리지 뱃지, 디플로이 뱃지 등의 목록을 반환합니다. 상속받은 그룹 뱃지도 함께 포함됩니다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

### Response

#### `200 OK`

```json
[
  {
    "id": 10,
    "name": "Coverage",
    "link_url": "https://gitlab.com/%{project_path}/-/jobs",
    "image_url": "https://gitlab.com/%{project_path}/badges/%{default_branch}/coverage.svg",
    "kind": "project"
  }
]
```

---

## 08. Create a badge for a project [POST]

### 기본 정보

- **기능:** 프로젝트에 신규 뱃지를 추가한다.
- **Endpoint:** `POST /api/v4/projects/{id}/badges`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

### Request

#### Body

| 필드 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `link_url` | string | Y | 뱃지 이동 URL 패턴 | `https://gitlab.com/%{project_path}/-/jobs` |
| `image_url` | string | Y | 뱃지 이미지 URL 패턴 | `https://gitlab.com/%{project_path}/badges/%{default_branch}/coverage.svg` |
| `name` | string | N | 뱃지 표시 이름 | `Coverage` |

```json
{
  "name": "Coverage",
  "link_url": "https://gitlab.com/%{project_path}/-/jobs",
  "image_url": "https://gitlab.com/%{project_path}/badges/%{default_branch}/coverage.svg"
}
```

### Response

#### `201 Created`

```json
{
  "id": 10,
  "name": "Coverage",
  "kind": "project"
}
```

---

## 09. Retrieve a badge preview for a project [GET]

### 기본 정보

- **기능:** 프로젝트 뱃지 렌더링 미리보기 결과를 반환한다.
- **Endpoint:** `GET /api/v4/projects/{id}/badges/render`
- **인증:** Bearer Token 필요

---

## 10. Retrieve a badge for a project [GET]

### 기본 정보

- **기능:** 프로젝트의 단일 뱃지 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요

---

## 11. Update a badge for a project [PUT]

### 기본 정보

- **기능:** 프로젝트 뱃지의 설정(링크, 이미지 URL 등)을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner

---

## 12. Delete a badge from a project [DEL]

### 기본 정보

- **기능:** 프로젝트 뱃지를 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/badges/{badge_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 Maintainer / Owner
