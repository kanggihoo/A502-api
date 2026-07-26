# 1. Report client performance metrics

## 기본 정보
- **기능**: 클라이언트 성능 측정값을 서버에 업로드한다.
- **Endpoint**: `POST /api/v4/client_perf`
- **인증**: 로그인 필요
- **권한**: 없음 (문서에 별도 권한 서술 없음, 클라이언트 성능 모니터링 기능의 일부로 일반 클라이언트가 호출)

## 설명
Client Performance Monitoring 기능의 일부로, 클라이언트에서 측정한 성능 지표(counter, histogram)를 서버에 보고하는 API이다. 스키마 버전(`version`)은 현재 "0.1.0"이어야 한다. 최소 서버 버전 9.9.0.

## Request

### Body
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| version | string | Yes | 제출 데이터의 스키마 식별자. 현재 "0.1.0"이어야 함 |
| client_id | string | No | 현재 사용되지 않음 |
| labels | string[] | No | 메트릭 백엔드에 기록될 때 모든 메트릭에 적용될 레이블 |
| start | integer | Yes | 이 보고서의 첫 메트릭 시각 (밀리초) |
| end | integer | Yes | 이 보고서의 마지막 메트릭 시각 (밀리초) |
| counters | object[] | No | 보고할 counter 메트릭 배열 |
| counters[].metric | string | Yes | counter 이름 |
| counters[].value | number | Yes | counter를 증가시킬 값 |
| counters[].timestamp | integer | No | counter가 증가된 시각 |
| counters[].labels | string[] | No | 이 메트릭에 적용될 레이블 |
| histograms | object[] | No | 보고할 histogram 측정값 배열 |
| histograms[].metric | string | Yes | 측정값 이름 |
| histograms[].value | number | Yes | 측정값 |
| histograms[].timestamp | integer | No | 측정이 수행된 시각 |
| histograms[].labels | string[] | No | 이 메트릭에 적용될 레이블 |

```json
{
  "version": "0.1.0",
  "labels": ["string"],
  "start": 0,
  "end": 0,
  "counters": [
    { "metric": "string", "value": 1, "timestamp": 0, "labels": ["string"] }
  ],
  "histograms": [
    { "metric": "string", "value": 1.5, "timestamp": 0, "labels": ["string"] }
  ]
}
```

## Response

### 200 - Measurements reported successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| status | string | 요청 성공 시 "ok" 반환 |

```json
{ "status": "ok" }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |
| 500 | 서버 오류 |

---
