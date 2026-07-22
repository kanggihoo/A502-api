# 138-저장소(Repositories) API 명세
### 1. 기여자 (Contributor)란?
- **Git 저장소에 코드를 작성해 커밋(Commit)한 개발자(팀원)**.
- API 응답: 개발자별 **이름, 이메일, 커밋 개수, 코드 추가 라인 수(+), 삭제 라인 수(-)** 집계 데이터.

---

### 2. Compare API 응답 및 "화면 제공" 방식

**맞음! API 응답은 100% JSON 형식.**

#### API가 주는 JSON 데이터 내용 (`GET /repository/compare`)
1. **`commits`**: 두 브랜치 사이에 쌓인 커밋 목록.
2. **`diffs`**: 파일별 코드 변경 내용 (코드 줄 추가/삭제 문자열).
3. **`web_url`**: GitLab 서버의 실제 Compare 웹 UI URL.

#### 활용(화면 제공) 방법 2가지
- **방안 A (원문 이동 링크)**: JSON의 `web_url`을 대시보드 버튼으로 만들어 **GitLab 웹 화면으로 즉시 이동**.
- **방안 B (커스텀 UI 렌더링)**: JSON의 `diffs` 텍스트를 받아 웹 프론트엔드의 **Diff 뷰어 컴포넌트로 예쁘게 표시**.

## 01-Get a project repository tree

## 기본 정보
- **기능:** 프로젝트 저장소의 디렉토리 트리를 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/tree`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트 저장소의 파일/디렉토리 트리 구조를 반환한다. 특정 경로나 브랜치 기준으로 조회할 수 있으며, 재귀적 조회도 가능하다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `ref` | string | N | 브랜치 또는 태그 이름 (기본 브랜치 사용) |
| `path` | string | N | 트리 경로 |
| `recursive` | boolean | N | 재귀적 트리 조회 여부 |
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `pagination` | string | N | 페이지네이션 방식 (recursive=true 시 "none"만 유효) |
| `page_token` | string | N | 키셋 페이지네이션 시작 레코드 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `id` | string | 항목 ID | `abc123...` |
| `name` | string | 파일/디렉토리명 | `src` |
| `type` | string | 타입 (`tree` 또는 `blob`) | `tree` |
| `path` | string | 전체 경로 | `src/main` |
| `mode` | string | 파일 모드 | `040000` |

JSON 예시:
```json
[
  {
    "id": "abc123def456",
    "name": "src",
    "type": "tree",
    "path": "src",
    "mode": "040000"
  },
  {
    "id": "def789ghi012",
    "name": "README.md",
    "type": "blob",
    "path": "README.md",
    "mode": "100644"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 02-Get raw blob contents from the repository

## 기본 정보
- **기능:** 저장소의 특정 Blob 원본 내용을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/blobs/{sha}/raw`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 SHA에 해당하는 Blob의 원본(raw) 내용을 반환한다. 파일 경로 대신 Blob SHA로 직접 접근할 때 사용한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |
| `sha` | string | Y | 커밋 해시 | `9b7d3c3...` |

## Response
### `200 OK`
Blob의 원본 내용을 본문(body)으로 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - Blob을 찾을 수 없음 |

---

## 04-Get an archive of the repository

## 기본 정보
- **기능:** 저장소를 아카이브 파일로 다운로드한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/archive`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
프로젝트 저장소를 아카이브(tar.gz, zip 등) 형식으로 다운로드한다. 특정 SHA, 형식, 하위 경로를 지정할 수 있으며 LFS Blob 제외 옵션도 제공한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `sha` | string | N | 다운로드할 아카이브의 커밋 SHA |
| `ref_type` | string | N | ref 유형 (`heads` 브랜치 또는 `tags` 태그) |
| `format` | string | N | 아카이브 형식 (예: `tar.gz`, `zip`, `tar`, `bz2`) |
| `path` | string | N | 다운로드할 저장소 하위 폴더 |
| `include_lfs_blobs` | boolean | N | LFS 객체 포함 여부 |
| `exclude_paths` | array | N | 아카이브에서 제외할 경로 목록 (쉼표 구분) |

## Response
### `200 OK`
아카이브 파일을 바이너리 스트림으로 반환한다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 05-Compare two branches, tags, or commits

## 기본 정보
- **기능:** 두 브랜치, 태그, 또는 커밋을 비교한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/compare`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
두 커밋/브랜치/태그 간의 차이점을 비교하여 커밋 목록과 diff를 반환한다. `from`과 `to`를 기준으로 비교하며, `straight` 파라미터로 비교 방식을 선택할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `from` | string | Y | 비교 시작 기준 (커밋 SHA, 브랜치명, 태그명) |
| `to` | string | Y | 비교 종료 기준 (커밋 SHA, 브랜치명, 태그명) |
| `from_project_id` | integer | N | 비교할 프로젝트 ID (다른 프로젝트 간 비교) |
| `straight` | boolean | N | 비교 방식 (true: `from`..`to` 직접 비교, false: `from`...`to` merge base 기준) |
| `unidiff` | boolean | N | Unified diff 형식으로 반환 |

## Response
### `200 OK`
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `commit` | object | 기준 커밋 정보 |
| `commits` | array[object] | `from`과 `to` 사이의 커밋 목록 |
| `diffs` | array[object] | 파일별 diff 목록 |
| `compare_timeout` | boolean | 비교 시간 초과 여부 |
| `compare_same_ref` | boolean | 동일한 참조 비교 여부 |
| `web_url` | string | 웹 UI 비교 URL |

각 diff 항목:
| 필드 | 타입 | 설명 |
|---|---:|---|---:|
| `diff` | string | diff 내용 |
| `collapsed` | boolean | diff 접힘 여부 |
| `too_large` | boolean | diff가 너무 큰지 여부 |
| `new_path` | string | 새 파일 경로 |
| `old_path` | string | 이전 파일 경로 |
| `new_file` | boolean | 새 파일 여부 |
| `renamed_file` | boolean | 파일명 변경 여부 |
| `deleted_file` | boolean | 삭제된 파일 여부 |
| `generated_file` | boolean | 생성된 파일 여부 |

JSON 예시:
```json
{
  "commit": {
    "id": "abc123",
    "short_id": "abc123",
    "title": "Base commit",
    "author_name": "John Doe",
    "author_email": "john@example.com"
  },
  "commits": [
    {
      "id": "def456",
      "short_id": "def456",
      "title": "Feature commit",
      "author_name": "Jane Doe",
      "author_email": "jane@example.com"
    }
  ],
  "diffs": [
    {
      "diff": "@@ -1 +1,2 @@\n+new line\n",
      "new_path": "README.md",
      "old_path": "README.md",
      "new_file": false,
      "renamed_file": false,
      "deleted_file": false
    }
  ],
  "compare_timeout": false,
  "compare_same_ref": false,
  "web_url": "https://gitlab.example.com/group/project/-/compare/main...feature"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 07-Get repository contributors

## 기본 정보
- **기능:** 저장소 기여자(Contributor) 목록을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/contributors`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 프로젝트 저장소의 기여자 목록을 이름, 이메일, 커밋 수, 추가/삭제 라인 수와 함께 반환한다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `page` | integer | N | 현재 페이지 번호 |
| `per_page` | integer | N | 페이지당 항목 수 |
| `ref` | string | N | 브랜치 또는 태그 이름 (기본 브랜치 사용) |
| `order_by` | string | N | 정렬 기준 (`name`, `email`, `commits`) |
| `sort` | string | N | 정렬 방향 (`asc` 또는 `desc`) |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `name` | string | 기여자 이름 | `John Doe` |
| `email` | string | 기여자 이메일 | `john@example.com` |
| `commits` | integer | 커밋 수 | `42` |
| `additions` | integer | 추가 라인 수 | `100` |
| `deletions` | integer | 삭제 라인 수 | `30` |

JSON 예시:
```json
[
  {
    "name": "John Doe",
    "email": "john@example.com",
    "commits": 42,
    "additions": 100,
    "deletions": 30
  },
  {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "commits": 15,
    "additions": 50,
    "deletions": 10
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |

---

## 09-Generates a changelog section for a release preview

## 기본 정보
- **기능:** 릴리스의 체인지로그 섹션을 생성하여 미리보기로 반환한다. (GitLab 14.6+)
- **Endpoint:** `GET /api/v4/projects/{id}/repository/changelog`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 버전의 릴리스에 대한 체인지로그 섹션을 생성한다. semantic versioning 형식의 `version`이 필수이며, 커밋 범위, 트레일러, 설정 파일 등을 지정할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | any | Y | 프로젝트 ID 또는 URL-인코딩된 경로 | `1234` or `group%2Fproject` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `version` | string | Y | semantic versioning 형식의 릴리스 버전 |
| `from` | string | N | 체인지로그에 포함할 커밋 범위의 시작 커밋 |
| `to` | string | N | 체인지로그에 포함할 커밋 범위의 마지막 커밋 |
| `date` | string | N | 릴리스 날짜 및 시간 (ISO 8601) |
| `trailer` | string | N | 체인지로그 포함 여부 결정에 사용할 Git 트레일러 |
| `config_file` | string | N | 체인지로그 설정 파일 경로 (기본값: `.gitlab/changelog_config.yml`) |
| `config_file_ref` | string | N | 설정 파일이 정의된 git 참조 (기본값: 기본 브랜치) |

## Response
### `200 OK`
| 필드 | 타입 | 설명 | 예시 |
|---|---:|---|---:|
| `notes` | string | 생성된 체인지로그 내용 (마크다운 형식) | `## 1.0.0\n\n### Features\n...` |

JSON 예시:
```json
{
  "notes": "## 1.0.0\n\n### Features\n- New feature added\n\n### Bug fixes\n- Bug fixed\n"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 프로젝트를 찾을 수 없음 |
