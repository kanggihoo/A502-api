# Repositories API 명세서 (관리자 권한 미필요 API)


---

## 01. Get a project repository tree [GET]

### 기본 정보

- **기능:** 프로젝트 저장소의 디렉토리 및 파일 구조(Tree) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/tree`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

지정한 브랜치(`ref`) 또는 특정 하위 경로(`path`)의 파일 및 디렉토리 구조를 조회합니다. `recursive=true` 옵션을 사용하여 전체 하위 경로 트리 구조를 한 번에 조회할 수 있습니다.

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
| `ref` | string | N | default branch | 조회할 브랜치명 또는 태그명 | `main` |
| `path` | string | N | 루트 디렉토리 | 조회할 하위 디렉토리 경로 | `src/main` |
| `recursive` | boolean | N | `false` | 하위 디렉토리 재귀적 조회 여부 | `true` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `id` | string | 파일 또는 디렉토리의 Git Blob/Tree SHA | `a1b2c3d4e5...` |
| `name` | string | 파일 또는 디렉토리 이름 | `App.java` |
| `type` | string | 항목 종류 (`tree` 또는 `blob`) | `blob` |
| `path` | string | 저장소 내 전체 경로 | `src/main/App.java` |
| `mode` | string | Git 파일 권한 모드 | `100644` |

```json
[
  {
    "id": "a1b2c3d4e5f6...",
    "name": "App.java",
    "type": "blob",
    "path": "src/main/App.java",
    "mode": "100644"
  },
  {
    "id": "f6e5d4c3b2a1...",
    "name": "resources",
    "type": "tree",
    "path": "src/main/resources",
    "mode": "040000"
  }
]
```

---

## 02. Get raw blob contents from the repository [GET]

### 기본 정보

- **기능:** 저장소 특정 파일(Blob)의 원본(Raw) 텍스트 또는 바이너리 데이터를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/blobs/{sha}/raw`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

파일의 SHA 해시값을 통해 해당 파일의 순수 원본 내용(Raw content)을 바이너리/텍스트 스트림 형태로 가져옵니다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID | `1234` |
| `sha` | string | Y | 파일(Blob)의 SHA-1 또는 SHA-256 해시값 | `a1b2c3d4e5...` |

### Response

#### `200 OK`
파일 원본 텍스트/바이너리 데이터 스트림 반환

---

## 03. Get a blob from the repository [GET]

### 기본 정보

- **기능:** 저장소 파일(Blob)의 메타데이터 및 Base64 인코딩된 콘텐츠를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/blobs/{sha}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Response

#### `200 OK`

```json
{
  "size": 1024,
  "encoding": "base64",
  "content": "cGFnZSBjb250ZW50...",
  "sha": "a1b2c3d4e5..."
}
```

---


## 05. Compare two branches, tags, or commits [GET]

### 기본 정보

- **기능:** 두 개의 브랜치, 태그, 또는 커밋 간의 차이점(Diff 및 커밋 목록)을 비교한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/compare`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

기준 지점(`from`)과 비교 지점(`to`) 사이의 변경 사항(커밋 히스토리 및 파일 변경 diff)을 조회합니다. 브랜치 간의 차이나 릴리즈 간의 변경 사항을 확인할 때 활용됩니다.

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `from` | string | Y | 기준 브랜치/태그명 또는 커밋 SHA | `main` |
| `to` | string | Y | 비교할 대상 브랜치/태그명 또는 커밋 SHA | `feature/login` |
| `straight` | boolean | N | `false` 필터 방식 (false: `from...to`, true: `from..to`) | `false` |

### Response

#### `200 OK`

```json
{
  "commit": {
    "id": "c1d2e3f4...",
    "title": "Add login feature"
  },
  "commits": [
    {
      "id": "c1d2e3f4...",
      "title": "Add login feature"
    }
  ],
  "diffs": [
    {
      "old_path": "src/Login.java",
      "new_path": "src/Login.java",
      "new_file": false,
      "renamed_file": false,
      "deleted_file": false,
      "diff": "@@ -1,3 +1,5 @@\n+import auth;\n"
    }
  ],
  "compare_timeout": false
}
```

---


## 07. Get repository contributors [GET]

### 기본 정보

- **기능:** 저장소 기여자(Contributors) 목록 및 각 기여자의 커밋/라인 수 통계를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/contributors`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `order_by` | string | N | `commits` | 정렬 기준 (`commits` \| `name` \| `email`) | `commits` |
| `sort` | string | N | `asc` | 정렬 방식 (`asc` \| `desc`) | `desc` |

### Response

#### `200 OK`

```json
[
  {
    "name": "홍길동",
    "email": "gildong@example.com",
    "commits": 42,
    "additions": 1500,
    "deletions": 300
  }
]
```

---


## 09. Generates a changelog section for a release and returns it [GET]

### 기본 정보

- **기능:** 릴리즈에 포함될 변경 이력(Changelog) 섹션 텍스트를 자동 생성하여 반환한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/changelog`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Developer 이상)

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `version` | string | Y | 생성할 릴리즈 버전 | `1.0.0` |
| `from` | string | N | 변경 이력 시작 커밋/태그 | `v0.9.0` |
| `to` | string | N | 변경 이력 종료 커밋/태그 | `v1.0.0` |

### Response

#### `200 OK`

```json
{
  "notes": "## 1.0.0 (2026-07-23)\n\n- Add new authentication API (#12)\n- Fix layout bug (#45)"
}
```

---


