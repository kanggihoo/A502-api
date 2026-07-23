# Releases API 명세서 (관리자 권한 미필요 API)
---

## 01. List all release links [GET]

### 기본 정보

- **기능:** 특정 릴리즈(Release)에 첨부된 자산 링크(Asset Links) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases/{tag_name}/assets/links`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트의 태그 이름(`tag_name`)에 지정된 릴리즈의 자산 다운로드/외부 링크(실행 파일, 런북, 패키지 등) 목록을 조회합니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |
| `tag_name` | string | Y | 릴리즈 태그 이름 | `v1.0.0` |

#### Query parameters

없음

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 자산 링크 ID | `1` |
| `name` | string | 링크 이름 | `release-binary.tar.gz` |
| `url` | string | 링크 다운로드 URL | `https://example.com/downloads/release-binary.tar.gz` |
| `link_type` | string | 링크 유형 (`package`, `image`, `runbook`, `other`) | `package` |

```json
[
  {
    "id": 1,
    "name": "release-binary.tar.gz",
    "url": "https://example.com/downloads/release-binary.tar.gz",
    "direct_asset_path": "/binaries/v1.0.0",
    "link_type": "package"
  }
]
```

---

## 02. Create a release link [POST]

### 기본 정보

- **기능:** 릴리즈에 자산 링크(Asset Link)를 새로 등록한다.
- **Endpoint:** `POST /api/v4/projects/{id}/releases/{tag_name}/assets/links`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

특정 릴리즈 항목에 실행 파일 URL, 이미지, 패키지, 런북 등의 다운로드 링크를 등록합니다. 링크 이름 및 URL은 해당 릴리즈 내에서 유일해야 합니다.

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
| `tag_name` | string | Y | 릴리즈 태그 이름 | `v1.0.0` |

#### Query parameters

없음

#### Body

| 필드 | 타입 | 필수 | 제약 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `name` | string | Y | - | 자산 링크 표시 이름 | `release-v1.0.0.apk` |
| `url` | string | Y | - | 링크 다운로드 URL | `https://example.com/builds/v1.0.0.apk` |
| `direct_asset_path` | string | N | - | 직접 자산 경로 | `/downloads/v1.0.0.apk` |
| `link_type` | string | N | `other` | 링크 유형 (`other` \| `runbook` \| `image` \| `package`) | `package` |

```json
{
  "name": "release-v1.0.0.apk",
  "url": "https://example.com/builds/v1.0.0.apk",
  "link_type": "package"
}
```

### Response

#### `201 Created`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | integer | 생성된 링크 ID | `10` |
| `name` | string | 링크 이름 | `release-v1.0.0.apk` |

```json
{
  "id": 10,
  "name": "release-v1.0.0.apk",
  "url": "https://example.com/builds/v1.0.0.apk",
  "link_type": "package"
}
```

---

## 03. Retrieve a release link [GET]

### 기본 정보

- **기능:** 특정 릴리즈의 단일 자산 링크 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

---

## 04. Update a release link [PUT]

### 기본 정보

- **기능:** 릴리즈 자산 링크의 이름, URL 또는 유형을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 05. Delete a release link [DEL]

### 기본 정보

- **기능:** 릴리즈 자산 링크를 삭제한다.
- **Endpoint:** `DELETE /api/v4/projects/{id}/releases/{tag_name}/assets/links/{link_id}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 06. List all releases in a group [GET]

### 기본 정보

- **기능:** 특정 그룹에 속한 전체 프로젝트의 릴리즈 목록을 조회한다.
- **Endpoint:** `GET /api/v4/groups/{id}/releases`
- **인증:** Bearer Token 필요
- **권한:** 그룹 멤버 (Reporter 이상)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 그룹 ID 또는 URL 인코딩 경로 | `my-group` |

### Response

#### `200 OK`

```json
[
  {
    "name": "Release v1.0.0",
    "tag_name": "v1.0.0",
    "description": "Initial stable release",
    "created_at": "2026-07-20T10:00:00Z"
  }
]
```

---

## 07. List all releases in a project [GET]

### 기본 정보

- **기능:** 프로젝트의 릴리즈 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩 경로 | `1234` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `order_by` | string | N | `released_at` | 정렬 필드 (`released_at` \| `created_at`) | `released_at` |
| `sort` | string | N | `desc` | 정렬 방식 (`asc` \| `desc`) | `desc` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

### Response

#### `200 OK`

```json
[
  {
    "name": "Version 1.0.0",
    "tag_name": "v1.0.0",
    "description": "## Release Notes\n- Add user authentication feature\n- Fix dashboard rendering bug",
    "created_at": "2026-07-23T12:00:00Z",
    "released_at": "2026-07-23T12:00:00Z",
    "upcoming_release": false
  }
]
```

---

## 08. Create a release [POST]

### 기본 정보

- **기능:** 프로젝트에 신규 릴리즈(Release)를 생성한다.
- **Endpoint:** `POST /api/v4/projects/{id}/releases`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### 설명

지정한 태그(`tag_name`) 또는 지정한 커밋/브랜치(`ref`)로부터 릴리즈를 생성합니다. 릴리즈 이름(`name`), 마크다운 설명(`description`), 관련 자산 링크(`assets.links`), 마일스톤(`milestones`) 등을 함께 지정할 수 있으며, SSAFY 팀 프로젝트의 배포 내역 및 릴리즈 노트 자동 등록에 활용됩니다.

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
| `tag_name` | string | Y | - | 릴리즈 기준 태그 이름 | `v1.0.0` |
| `name` | string | N | - | 릴리즈 표시 제목 | `S15P11A502 v1.0.0 정식 배포` |
| `description` | string | N | Markdown 지원 | 릴리즈 상세 설명/노트 | `## 변경사항\n- API 통합 완료` |
| `ref` | string | N | - | 태그 미존재 시 태그를 생성할 대상(브랜치/커밋 SHA) | `main` |
| `released_at` | string | N | ISO 8601 | 릴리즈 일시 (기본값: 현재 시각) | `2026-07-23T13:00:00Z` |

```json
{
  "tag_name": "v1.0.0",
  "name": "S15P11A502 v1.0.0 정식 배포",
  "description": "## 변경사항\n- API 통합 완료\n- Mattermost 알림 연동",
  "ref": "main"
}
```

### Response

#### `201 Created`

```json
{
  "name": "S15P11A502 v1.0.0 정식 배포",
  "tag_name": "v1.0.0",
  "description": "## 변경사항\n- API 통합 완료\n- Mattermost 알림 연동",
  "created_at": "2026-07-23T13:00:00Z",
  "released_at": "2026-07-23T13:00:00Z",
  "upcoming_release": false
}
```

---

## 09. Retrieve a release by tag name [GET]

### 기본 정보

- **기능:** 태그 이름으로 특정 릴리즈의 상세 정보를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/releases/{tag_name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

---

## 10. Update a release [PUT]

### 기본 정보

- **기능:** 기존 릴리즈의 이름, 설명, 마일스톤 또는 릴리즈 시각을 수정한다.
- **Endpoint:** `PUT /api/v4/projects/{id}/releases/{tag_name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 11. Delete a release [DEL]

### 기본 정보

- **기능:** 특정 릴리즈 항목을 삭제한다 (Git 태그는 삭제되지 않고 유지됨).
- **Endpoint:** `DELETE /api/v4/projects/{id}/releases/{tag_name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

---

## 12. Generate release evidence [POST]

### 기본 정보

- **기능:** 특정 릴리즈에 대한 증빙(Evidence) JSON 데이터를 생성한다.
- **Endpoint:** `POST /api/v4/projects/{id}/releases/{tag_name}/evidence`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)
