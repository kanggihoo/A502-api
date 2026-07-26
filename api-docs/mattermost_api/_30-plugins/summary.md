# 7. Get webapp plugins

## 기본 정보
- **기능**: 서버에 설치되고 활성화된 웹앱 플러그인 목록을 조회한다.
- **Endpoint**: `GET /api/v4/plugins/webapp`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
서버에 설치되어 활성화된 웹앱 플러그인 목록을 반환한다. 최소 서버 버전은 4.4이다.

## Request

파라미터 없음.

## Response

### 200 - 성공
| 필드 | 타입 | 설명 |
|---|---|---|
| id | string | 플러그인을 나타내는 전역 고유 식별자 |
| version | string | 플러그인 버전 |
| webapp.bundle_path | string | 웹앱 JavaScript 번들 경로 |

```json
[
  {
    "id": "string",
    "version": "string",
    "webapp": {
      "bundle_path": "string"
    }
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |

---

# 8. Get plugins status

## 기본 정보
- **기능**: 클러스터 전체에 설치된 플러그인들의 상태를 조회한다.
- **Endpoint**: `GET /api/v4/plugins/statuses`
- **인증**: Bearer Token 불필요
- **권한**: 없음

## 설명
클러스터 내 어디든 설치된 플러그인들의 상태를 반환한다. 최소 서버 버전은 4.4이다.

## Request

파라미터 없음.

## Response

### 200 - Plugin status retreived successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| plugin_id | string | 플러그인을 나타내는 전역 고유 식별자 |
| name | string | 플러그인 이름 |
| description | string | 플러그인에 대한 설명 |
| version | string | 플러그인 버전 |
| cluster_id | string | 플러그인이 실행 중인 클러스터의 ID |
| plugin_path | string | 서버상의 플러그인 경로 |
| state | enum | 플러그인 상태 ("NotRunning", "Starting", "Running", "FailedToStart", "FailedToStayRunning", "Stopping") |

```json
[
  {
    "plugin_id": "string",
    "name": "string",
    "description": "string",
    "version": "string",
    "cluster_id": "string",
    "plugin_path": "string",
    "state": "Running"
  }
]
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 명시되지 않음 |
| 401 | 명시되지 않음 |
| 403 | 명시되지 않음 |
| 501 | 명시되지 않음 |
