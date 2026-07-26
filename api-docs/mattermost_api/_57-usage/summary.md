# 1. Get current usage of posts

## 기본 정보
- **기능**: 인스턴스의 전체 게시글 수(반올림된 근사값)를 조회한다.
- **Endpoint**: `GET /api/v4/usage/posts`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
이 인스턴스의 전체 게시글 수를 유효 숫자 기준으로 내림/반올림한 근사값으로 조회하는 API이다 (예: 4321 대신 4000 반환). 최소 서버 버전은 7.0이다.

## Response

### 200 - Total no. of posts returned successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| count | number | 전체 게시글 수 (근사값) |

```json
{ "count": 4000 }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

## 주의 사항
정확한 값이 아니라 반올림된 근사값을 반환한다.

---

# 2. Get the total file storage usage for the instance in bytes

## 기본 정보
- **기능**: 인스턴스의 전체 파일 스토리지 사용량(바이트)을 조회한다.
- **Endpoint**: `GET /api/v4/usage/storage`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
이 인스턴스의 전체 파일 스토리지 사용량을 바이트 단위로, 최상위 유효 숫자 기준으로 내림한 근사값으로 조회하는 API이다 (예: 4321 대신 4000 반환). 최소 서버 버전은 7.1이다.

## Response

### 200 - Total file storage usage in bytes
| 필드 | 타입 | 설명 |
|---|---|---|
| bytes | number | 전체 파일 스토리지 사용량 (바이트, 근사값) |

```json
{ "bytes": 4000 }
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

## 주의 사항
정확한 값이 아니라 내림된 근사값을 반환한다.

---

# 3. Get current usage of teams

## 기본 정보
- **기능**: 인스턴스의 전체 팀 수(반올림된 근사값)를 조회한다.
- **Endpoint**: `GET /api/v4/usage/teams`
- **인증**: Bearer Token 필요
- **권한**: 없음 (인증만 필요)

## 설명
이 인스턴스의 전체 팀 수를 반올림된 근사값으로 조회하는 API이다.

## Response

### 200 - Total number of teams returned successfully
| 필드 | 타입 | 설명 |
|---|---|---|
| active | integer | 활성 팀 수 |
| cloud_archived | integer | 클라우드 아카이브된 팀 수 |
| teams | integer | 전체 팀 수 |

```json
{
  "active": 0,
  "cloud_archived": 0,
  "teams": 0
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 401 | 인증되지 않음 |
| 500 | 서버 오류 |

---
