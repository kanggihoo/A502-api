# 1. Search files in a team

## 기본 정보
- **기능**: 현재 사용자가 속한 팀에서 파일 이름·확장자·파일 내용으로 파일을 검색한다.
- **Endpoint**: `POST /api/v4/files/search`
- **인증**: Bearer Token 필요
- **권한**: `view_team`

## 설명
파일 이름, 확장자, 파일 내용(파일 내용 추출이 활성화되어 있고 해당 파일 형식이 지원되는 경우)을 기준으로 현재 사용자의 팀 내 파일을 검색하는 API이다. `from:사용자명`, `in:채널명`, `ext:확장자` 형식의 검색 연산자를 지원한다. 최소 서버 버전은 10.2이다.

## Request

### Body (multipart/form-data)
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| terms | string | Yes | 검색어. `from:someusername`(사용자별), `in:somechannel`(채널 이름 기준, 표시 이름 아님), `ext:extension`(확장자별) 사용 가능 |
| is_or_search | boolean | Yes | true면 OR 검색, false면 AND 검색 |
| time_zone_offset | integer | No | 날짜 검색용 사용자 시간대의 UTC 오프셋 |
| include_deleted_channels | boolean | No | true면 삭제(아카이브)된 채널도 검색에 포함 |
| page | integer | No | 조회할 페이지 (Elasticsearch에서만 동작) |
| per_page | integer | No | 페이지당 게시글 수 (Elasticsearch에서만 동작) |

## Response

### 200 - Files list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| order | array(string) | 파일 정렬 순서 |
| file_infos | object | 파일 정보 맵 |
| next_file_id | string | 다음 파일 정보의 ID |
| prev_file_id | string | 이전 파일 정보의 ID |

```json
{
  "order": ["string"],
  "file_infos": {},
  "next_file_id": "string",
  "prev_file_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
page/per_page 페이지네이션은 Elasticsearch가 활성화된 경우에만 동작한다.

---

# 2. Search files across the teams of the current user

## 기본 정보
- **기능**: 현재 사용자가 속한 팀들 전체에서 파일 이름·확장자·파일 내용으로 파일을 검색한다.
- **Endpoint**: `POST /api/v4/files/search`
- **인증**: Bearer Token 필요
- **권한**: `view_team`

## 설명
파일 이름, 확장자, 파일 내용(파일 내용 추출이 활성화되어 있고 해당 파일 형식이 지원되는 경우)을 기준으로 현재 사용자가 속한 팀들에서 파일을 검색하는 API이다. 요청/응답 구조는 팀 단위 파일 검색과 동일하다. 최소 서버 버전은 10.2이다.

## Request

### Body (multipart/form-data)
| 필드 | 타입 | 필수 | 설명 |
|---|---|---|---|
| terms | string | Yes | 검색어. `from:someusername`(사용자별), `in:somechannel`(채널 이름 기준, 표시 이름 아님), `ext:extension`(확장자별) 사용 가능 |
| is_or_search | boolean | Yes | true면 OR 검색, false면 AND 검색 |
| time_zone_offset | integer | No | 날짜 검색용 사용자 시간대의 UTC 오프셋 |
| include_deleted_channels | boolean | No | true면 삭제(아카이브)된 채널도 검색에 포함 |
| page | integer | No | 조회할 페이지 (Elasticsearch에서만 동작) |
| per_page | integer | No | 페이지당 게시글 수 (Elasticsearch에서만 동작) |

## Response

### 200 - Files list retrieval successful
| 필드 | 타입 | 설명 |
|---|---|---|
| order | array(string) | 파일 정렬 순서 |
| file_infos | object | 파일 정보 맵 |
| next_file_id | string | 다음 파일 정보의 ID |
| prev_file_id | string | 이전 파일 정보의 ID |

```json
{
  "order": ["string"],
  "file_infos": {},
  "next_file_id": "string",
  "prev_file_id": "string"
}
```

## Errors
| 상태 코드 | 설명 |
|---|---|
| 400 | 잘못된 요청 |
| 401 | 인증되지 않음 |
| 403 | 권한 없음 |

## 주의 사항
page/per_page 페이지네이션은 Elasticsearch가 활성화된 경우에만 동작한다.

---
