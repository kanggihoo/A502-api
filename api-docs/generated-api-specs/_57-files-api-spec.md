# 57-파일(Files) API 명세
Raw API는 단일 파일 전용. 여러 개 가져오려면 개별 병렬(Concurrent) 호출 필요.
### 대안 (여러 파일 한 번에 가져올 때)

1. GraphQL API 사용 (추천):
  • 단 1번의 GraphQL 요청으로 여러 파일의 내용 묶어서 조회 가능.
2. Repository Archive API (GET /projects/{id}/repository/archive):
  • 저장소 전체(또는 특정 폴더)를 .zip / .tar.gz 묶음으로 1번에 다운로드 후 압축 해제.
## 03-Retrieve a raw file from a repository

## 기본 정보
- **기능:** 저장소의 특정 파일 원본(raw) 내용을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/files/{file_path}/raw`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 파일의 원본(raw) 내용을 반환한다. LFS 포인터 파일의 경우 `lfs` 파라미터로 바이너리 데이터를 조회할 수 있다. 응답은 일반 텍스트 또는 바이너리 형식으로 반환된다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID | `1234` |
| `file_path` | string | Y | URL-인코딩된 파일 경로 | `src%2Fmain%2Fapp.js` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `ref` | string | N | 브랜치, 태그 또는 커밋 이름 (기본 브랜치 사용) |
| `lfs` | boolean | N | LFS 포인터 파일의 바이너리 데이터 조회 |

## Response
### `200 OK`
파일의 원본 내용을 본문(body)으로 반환한다. 응답 형식은 파일의 MIME 타입에 따라 달라진다.

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 파일을 찾을 수 없음 |

---

## 05-Retrieve a file from a repository

## 기본 정보
- **기능:** 저장소의 특정 파일 정보와 내용을 조회한다.
- **Endpoint:** `GET /api/v4/projects/{id}/repository/files/{file_path}`
- **인증:** Bearer Token 필요
- **권한:** `read_api`
- **멱등성:** 지원

## 설명
지정된 파일의 메타데이터(이름, 크기)와 Base64로 인코딩된 내용을 반환한다. `ref` 파라미터가 필수이며, 특정 브랜치/태그/커밋 시점의 파일을 조회할 수 있다.

## Request
### Headers
| 이름 | 필수 | 설명 | 예시 |
|---|---:|---|---|
| `Authorization` | Y | 액세스 토큰 | `Bearer {accessToken}` |

### Path parameters
| 이름 | 타입 | 필수 | 설명 | 예시 |
|---|---:|---|---:|---|
| `id` | string | Y | 프로젝트 ID | `1234` |
| `file_path` | string | Y | URL-인코딩된 파일 경로 | `src%2Fmain%2Fapp.js` |

### Query parameters
| 이름 | 타입 | 필수 | 설명 |
|---|---:|---|---:|
| `ref` | string | Y | 브랜치, 태그 또는 커밋 이름 |

## Response
### `200 OK`
파일 정보를 JSON으로 반환한다. (상세 필드는 GitLab API 문서 참조)

## Errors
| 상태 코드 | 설명 |
|---|---:|
| `400` | Bad Request - 잘못된 요청 |
| `404` | Not Found - 파일을 찾을 수 없음 |
