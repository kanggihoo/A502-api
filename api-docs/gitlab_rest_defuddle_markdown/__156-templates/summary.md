# Templates API 명세서 (관리자 권한 미필요 API)

본 문서는 `_156-templates` 디렉토리 내의 GitLab Templates (전역 템플릿: License, .gitignore, GitLab CI/CD YAML, Dockerfile) 관련 API 중 일반 사용자 및 프로젝트 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 8개)

---

## 01. List all license templates [GET]

### 기본 정보

- **기능:** GitLab 인스턴스에서 사용 가능한 오픈소스 라이선스 템플릿 목록을 조회한다.
- **Endpoint:** `GET /api/v4/templates/licenses`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자 (인증된 일반 유저)

### 설명

프로젝트에 적용할 수 있는 표준 오픈소스 라이선스(MIT, Apache-2.0, GPL-3.0 등) 목록을 가져옵니다. `popular=true` 파라미터를 사용하여 자주 쓰이는 주요 라이선스만 필터링 조회할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | N | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

없음

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `popular` | boolean | N | - | 인기 있는 주류 라이선스만 필터링 | `true` |
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `key` | string | 라이선스 고유 키 | `mit` |
| `name` | string | 라이선스 이름 | `MIT License` |
| `popular` | boolean | 인기 라이선스 여부 | `true` |

```json
[
  {
    "key": "mit",
    "name": "MIT License",
    "popular": true
  },
  {
    "key": "apache-2.0",
    "name": "Apache License 2.0",
    "popular": true
  }
]
```

---

## 02. Retrieve a license template [GET]

### 기본 정보

- **기능:** 특정 오픈소스 라이선스 템플릿의 상세 설명, 조건 및 본문을 조회한다.
- **Endpoint:** `GET /api/v4/templates/licenses/{key}`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### 설명

지정한 라이선스 키(`key`)에 해당하는 템플릿 본문(`content`), 허용 사항(`permissions`), 제한 사항(`limitations`), 필요 조건(`conditions`) 등의 메타데이터를 조회합니다. `project` 및 `fullname` 파라미터로 저작권자 플레이스홀더를 자동 변환할 수 있습니다.

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `key` | string | Y | 라이선스 키 | `mit` |

#### Query parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `project` | string | N | 저작권 플레이스홀더 치환용 프로젝트 이름 | `S15P11A502` |
| `fullname` | string | N | 저작권자 전체 이름 | `SSAFY Team` |

### Response

#### `200 OK`

```json
{
  "key": "mit",
  "name": "MIT License",
  "nickname": "MIT",
  "html_url": "http://choosealicense.com/licenses/mit/",
  "source_url": "https://opensource.org/licenses/MIT",
  "popular": true,
  "description": "A short and simple permissive license...",
  "conditions": [ "include-copyright" ],
  "permissions": [ "commercial-use", "modifications", "distribution" ],
  "limitations": [ "no-liability" ],
  "content": "MIT License\n\nCopyright (c) 2026 SSAFY Team..."
}
```

---

## 03. List all .gitignore templates [GET]

### 기본 정보

- **기능:** 제공되는 표준 `.gitignore` 템플릿 목록을 조회한다.
- **Endpoint:** `GET /api/v4/templates/gitignores`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### 설명

다양한 언어 및 프레임워크(Java, Node, Python, Go 등)를 위한 표준 `.gitignore` 템플릿 목록을 조회합니다. 프로젝트 생성 및 초기 구성 시 `.gitignore` 파일 보급을 보조합니다.

### Request

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

### Response

#### `200 OK`

```json
[
  {
    "key": "Java",
    "name": "Java"
  },
  {
    "key": "Node",
    "name": "Node"
  }
]
```

---

## 04. Retrieve a .gitignore template [GET]

### 기본 정보

- **기능:** 특정 언어/환경의 `.gitignore` 템플릿 본문 텍스트를 조회한다.
- **Endpoint:** `GET /api/v4/templates/gitignores/{key}`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### Request

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `key` | string | Y | .gitignore 템플릿 키 | `Java` |

### Response

#### `200 OK`

```json
{
  "name": "Java",
  "content": "*.class\n*.log\n*.jar\n*.war\n.idea/\ntarget/\nbuild/\n"
}
```

---

## 05. List all GitLab CI/CD YAML templates [GET]

### 기본 정보

- **기능:** 제공되는 표준 `.gitlab-ci.yml` 파이프라인 템플릿 목록을 조회한다.
- **Endpoint:** `GET /api/v4/templates/gitlab_ci_ymls`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### Response

#### `200 OK`

```json
[
  {
    "key": "Android",
    "name": "Android"
  },
  {
    "key": "Maven",
    "name": "Maven"
  }
]
```

---

## 06. Retrieve a GitLab CI/CD YAML template [GET]

### 기본 정보

- **기능:** 특정 파이프라인 `.gitlab-ci.yml` 템플릿의 본문을 조회한다.
- **Endpoint:** `GET /api/v4/templates/gitlab_ci_ymls/{key}`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### Response

#### `200 OK`

```json
{
  "name": "Maven",
  "content": "image: maven:3.8.5-openjdk-17\n\nstages:\n  - build\n  - test\n"
}
```

---

## 07. List all Dockerfile templates [GET]

### 기본 정보

- **기능:** 제공되는 표준 `Dockerfile` 템플릿 목록을 조회한다.
- **Endpoint:** `GET /api/v4/templates/dockerfiles`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### Response

#### `200 OK`

```json
[
  {
    "key": "Binary",
    "name": "Binary"
  }
]
```

---

## 08. Retrieve a Dockerfile template [GET]

### 기본 정보

- **기능:** 특정 `Dockerfile` 템플릿의 본문 텍스트를 조회한다.
- **Endpoint:** `GET /api/v4/templates/dockerfiles/{key}`
- **인증:** Bearer Token 필요 / 선택 사항
- **권한:** 모든 사용자

### Response

#### `200 OK`

```json
{
  "name": "Binary",
  "content": "FROM scratch\nEXPOSE 8080\nCOPY app /app\nENTRYPOINT [\"/app\"]\n"
}
```
