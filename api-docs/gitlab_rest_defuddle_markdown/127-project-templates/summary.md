# Project Templates API 명세서 (관리자 권한 미필요 API)

본 문서는 `_127-project-templates` 디렉토리 내의 GitLab Project Templates 관련 API 중 일반 사용자 및 프로젝트 멤버 권한으로 호출 가능한 API들을 표준 템플릿에 맞추어 정리한 문서입니다. (총 2개)

---

## 01. List all templates of a particular type [GET]

### 기본 정보

- **기능:** 프로젝트에서 사용 가능한 특정 유형(Type)의 템플릿 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/templates/{type}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

프로젝트에 적용할 수 있는 특정 유형의 템플릿 목록(`key`, `name`)을 가져옵니다. 지원되는 템플릿 유형에는 `dockerfiles`, `gitignores`, `gitlab_ci_ymls`, `licenses`, `issues`, `merge_requests`가 있습니다. 템플릿 선택 UI 구성을 위해 템플릿 종류를 목록화할 때 사용됩니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1234` |
| `type` | string | Y | 템플릿 유형 (`dockerfiles` \| `gitignores` \| `gitlab_ci_ymls` \| `licenses` \| `issues` \| `merge_requests`) | `gitignores` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `page` | integer | N | `1` | 페이지 번호 | `1` |
| `per_page` | integer | N | `20` | 페이지당 항목 수 | `20` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `key` | string | 템플릿 고유 식별 키 | `Go` |
| `name` | string | 템플릿 표시 이름 | `Go` |

```json
[
  {
    "key": "Go",
    "name": "Go"
  },
  {
    "key": "Node",
    "name": "Node"
  }
]
```

---

## 02. Retrieve a template of a particular type [GET]

### 기본 정보

- **기능:** 프로젝트에서 지정한 유형 및 이름의 템플릿 상세 내용(본문 및 메타데이터)을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/templates/{type}/{name}`
- **인증:** Bearer Token 필요
- **권한:** 프로젝트 멤버 (Guest 이상)

### 설명

특정 유형(`type`)과 템플릿 키 이름(`name`)에 해당하는 템플릿 본문 및 조건 메타데이터를 가져옵니다. 오픈소스 라이선스(`licenses`) 조회 시에는 프로젝트 이름(`project`) 및 저작권자 이름(`fullname`) 파라미터를 추가하여 라이선스 내 플레이스홀더를 치환할 수 있습니다.

### Request

#### Headers

| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

#### Path parameters

| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---|---:|---|---|
| `id` | string/integer | Y | 프로젝트 ID 또는 URL 인코딩된 경로 | `1234` |
| `type` | string | Y | 템플릿 유형 (`dockerfiles` \| `gitignores` \| `gitlab_ci_ymls` \| `licenses` \| `issues` \| `merge_requests`) | `licenses` |
| `name` | string | Y | 목록 조회를 통해 얻은 템플릿 키 | `mit` |

#### Query parameters

| 이름 | 타입 | 필수 | 기본값 | 설명 | 예시 |
|---|---|---:|---|---|---|
| `source_template_project_id` | integer | N | - | 템플릿이 저장된 원본 프로젝트 ID | `567` |
| `project` | string | N | - | 라이선스 치환용 프로젝트 이름 (licenses 전용) | `MyAwesomeApp` |
| `fullname` | string | N | - | 라이선스 치환용 저작권자 전체 이름 (licenses 전용) | `Hong Gildong` |

#### Body

없음

### Response

#### `200 OK`

| 필드 | 타입 | 설명 | 예시 |
|---|---|---|---|
| `key` | string | 템플릿 키 | `mit` |
| `name` | string | 템플릿 이름 | `MIT License` |
| `content` | string | 템플릿 본문 텍스트 내용 | `MIT License\n\nCopyright (c)...` |
| `description` | string | 템플릿 설명 | `A short and simple permissive license...` |
| `conditions` | array | 라이선스 조건 항목 배열 | `["include-copyright"]` |
| `permissions` | array | 라이선스 허용 항목 배열 | `["commercial-use", "modifications"]` |

```json
{
  "key": "mit",
  "name": "MIT License",
  "nickname": "MIT",
  "html_url": "http://choosealicense.com/licenses/mit/",
  "source_url": "https://opensource.org/licenses/MIT",
  "popular": true,
  "description": "A short and simple permissive license with conditions...",
  "conditions": [
    "include-copyright"
  ],
  "permissions": [
    "commercial-use",
    "modifications",
    "distribution",
    "private-use"
  ],
  "limitations": [
    "no-liability"
  ],
  "content": "MIT License\n\nCopyright (c) 2026 Hong Gildong..."
}
```
